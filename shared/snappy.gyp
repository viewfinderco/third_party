{
  'targets': [
    {
      'target_name': 'libsnappy',
      'type': 'static_library',
      'include_dirs': [
        'snappy',
      ],
      'all_dependent_settings': {
        'include_dirs': [
          'snappy',
        ],
      },
      'sources': [
        'snappy/snappy-internal.h',
        'snappy/snappy-sinksource.cc',
        'snappy/snappy-sinksource.h',
        'snappy/snappy-stubs-internal.cc',
        'snappy/snappy-stubs-internal.h',
        'snappy/snappy.cc',
        'snappy/snappy.h',
      ],
      # snappy-stubs-internal.h unapologetically has: using namespace std
      # https://code.google.com/p/snappy/issues/detail?id=70
      'xcode_settings': {
        'WARNING_CFLAGS!': [ '-Wheader-hygiene' ],
      },
      'cflags!': [ '-Wheader-hygiene' ],
    },
  ],
}
