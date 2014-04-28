{
  # TODO(ben): why is this boilerplate necessary in every gyp file that uses protos?
  'target_defaults': {
    'default_configuration': 'Debug',
    'configurations': {
      'Debug': {},
      'Release': {},
      'Ad-hoc': {},
      'AppStore': {},
      'Enterprise': {},
    },
  },
  'targets': [
     {
      'target_name': 'libplcrashreporter',
      'type': 'static_library',
      'sources': [
        'plcrashreporter/Source/CrashReporter.m',
        #'plcrashreporter/Source/Fuzz/fuzz-main.m',
        #'plcrashreporter/Source/PLCrashAsyncImageListTests.m',
        #'plcrashreporter/Source/PLCrashAsyncLocalSymbolicationTests.m',
        #'plcrashreporter/Source/PLCrashAsyncMachOImageTests.m',
        #'plcrashreporter/Source/PLCrashAsyncMachOStringTests.m',
        #'plcrashreporter/Source/PLCrashAsyncMObjectTests.m',
        #'plcrashreporter/Source/PLCrashAsyncObjCSectionTests.m',
        #'plcrashreporter/Source/PLCrashAsyncSignalInfoTests.m',
        #'plcrashreporter/Source/PLCrashAsyncTests.m',
        #'plcrashreporter/Source/PLCrashFrameWalkerTests.m',
        'plcrashreporter/Source/PLCrashLogWriter.m',
        'plcrashreporter/Source/PLCrashLogWriter_trampoline.m',
        #'plcrashreporter/Source/PLCrashLogWriterTests.m',
        'plcrashreporter/Source/PLCrashReportApplicationInfo.m',
        'plcrashreporter/Source/PLCrashReportBinaryImageInfo.m',
        'plcrashreporter/Source/PLCrashReporter.m',
        'plcrashreporter/Source/PLCrashReporterNSError.m',
        #'plcrashreporter/Source/PLCrashReporterNSErrorTests.m',
        #'plcrashreporter/Source/PLCrashReporterTests.m',
        'plcrashreporter/Source/PLCrashReportExceptionInfo.m',
        'plcrashreporter/Source/PLCrashReportMachineInfo.m',
        'plcrashreporter/Source/PLCrashReportProcessInfo.m',
        'plcrashreporter/Source/PLCrashReportProcessorInfo.m',
        'plcrashreporter/Source/PLCrashReportSignalInfo.m',
        'plcrashreporter/Source/PLCrashReportSystemInfo.m',
        #'plcrashreporter/Source/PLCrashReportTests.m',
        'plcrashreporter/Source/PLCrashReportTextFormatter.m',
        'plcrashreporter/Source/PLCrashReportThreadInfo.m',
        'plcrashreporter/Source/PLCrashSignalHandler.m',
        #'plcrashreporter/Source/PLCrashSignalHandlerTests.m',
        #'plcrashreporter/Source/PLCrashSysctlTests.m',

        'plcrashreporter/Source/PLCrashAsync.c',
        'plcrashreporter/Source/PLCrashAsyncImageList.c',
        'plcrashreporter/Source/PLCrashAsyncLocalSymbolication.c',
        'plcrashreporter/Source/PLCrashAsyncMachOImage.c',
        'plcrashreporter/Source/PLCrashAsyncMachOString.c',
        'plcrashreporter/Source/PLCrashAsyncMObject.c',
        'plcrashreporter/Source/PLCrashAsyncObjCSection.c',
        'plcrashreporter/Source/PLCrashAsyncSignalInfo.c',
        'plcrashreporter/Source/PLCrashFrameWalker.c',
        'plcrashreporter/Source/PLCrashFrameWalker_arm.c',
        'plcrashreporter/Source/PLCrashFrameWalker_i386.c',
        'plcrashreporter/Source/PLCrashFrameWalker_ppc.c',
        'plcrashreporter/Source/PLCrashFrameWalker_x86_64.c',
        'plcrashreporter/Source/PLCrashLogWriterEncoding.c',
        'plcrashreporter/Source/PLCrashSysctl.c',

        'plcrashreporter/Source/PLCrashLogWriter_trampoline_asm.S',

        'plcrashreporter/Source/PLCrashReport.mm',
        'plcrashreporter/Source/PLCrashReportSymbolicate.mm',

        'plcrashreporter/Resources/crash_report.proto',
      ],
      'include_dirs': [
        '${SHARED_INTERMEDIATE_DIR}',  # for protos
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          'plcrashreporter/Source',
        ],
      },
      'dependencies': [
	'../shared/protobuf.gyp:libprotobuf',
      ],
      'includes': [
        '../../clients/shared/protoc.gypi',
      ],
      'xcode_settings': {
        'WARNING_CFLAGS': [
          '-Wno-incompatible-pointer-types',
        ],
      },
    },
 ],
}
