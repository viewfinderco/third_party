#import <map>
#import <string>
#import <cxxabi.h>
#import <dlfcn.h>
#import <string.h>
extern "C" {
#import "PLCrashAsyncImageList.h"
#import "PLCrashAsyncMachOImage.h"
#import "PLCrashReportSymbolicate.h"
#import "PLCrashReporter.h"
}  // extern "C"

namespace {

using std::string;
using std::map;

string DemangleSymbol(const char* symbol) {
  int status;
  char* buf = abi::__cxa_demangle(symbol, NULL, 0, &status);
  if (buf) {
    const string r(buf);
    free(buf);
    return r;
  }
  return symbol;
}

class Symbolicator {
  typedef map<string, const char*> BaseAddrMap;

 public:
  Symbolicator() {
    plcrash_async_image_list_t* image_list = [PLCrashReporter sharedImageList];
    plcrash_async_image_list_set_reading(image_list, true);

    plcrash_async_image_t *image = NULL;
    while ((image = plcrash_async_image_list_next(image_list, image)) != NULL) {
      struct uuid_command uuid;
      pl_vm_address_t uuid_addr = pl_async_macho_find_command(
          &image->macho_image, LC_UUID, &uuid, sizeof(uuid));
      if (uuid_addr != 0) {
        string uuid_str(sizeof(uuid.uuid) * 2, ' ');
        const char hex[] = "0123456789abcdef";
        for (int i = 0; i < sizeof(uuid.uuid); i++) {
          const uint8_t c = uuid.uuid[i];
          uuid_str[i * 2 + 0] = hex[c >> 4];
          uuid_str[i * 2 + 1] = hex[c & 0x0F];
        }
        base_addr_[uuid_str] = (const char*)image->macho_image.header_addr;
      }
    }

    plcrash_async_image_list_set_reading(image_list, false);

  }
  ~Symbolicator() {
  }

  string Symbolicate(NSString* image_uuid, uint64_t offset) const {
    const string u([image_uuid UTF8String]);
    BaseAddrMap::const_iterator iter(base_addr_.find(u));
    if (iter == base_addr_.end()) {
      return string();
    }
    const void* full_addr = iter->second + offset;
    Dl_info info;
    if (dladdr(full_addr, &info) == 0) {
      return string();
    }
    const string demangled = DemangleSymbol(info.dli_sname);
    if (demangled == "<redacted>") {
      return "";
    }
    return " " + demangled;
  }

 private:
  BaseAddrMap base_addr_;
};

}  // namespace

void* PLCrashReportSymbolicatorCreate() {
  return new Symbolicator();
}

void PLCrashReportSymbolicatorDestroy(void* symbolicator) {
  Symbolicator* s = reinterpret_cast<Symbolicator*>(symbolicator);
  delete s;
}

NSString* PLCrashReportSymbolicate(
    void* symbolicator, NSString* image_uuid, uint64_t offset) {
  Symbolicator* s = reinterpret_cast<Symbolicator*>(symbolicator);
  const string r = s->Symbolicate(image_uuid, offset);
  if (r.empty()) {
    return @"";
  }
  return [[NSString alloc] initWithBytes:r.data()
                                  length:r.size()
                                encoding:NSUTF8StringEncoding];
}

// local variables:
// mode: c++
// end:
