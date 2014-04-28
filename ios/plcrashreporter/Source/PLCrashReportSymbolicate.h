#import <Foundation/Foundation.h>

void* PLCrashReportSymbolicatorCreate();
void PLCrashReportSymbolicatorDestroy(void* symbolicator);
NSString* PLCrashReportSymbolicate(
    void* symbolicator, NSString* image_uuid, uint64_t offset);
