{
  'conditions': [
    ['OS=="ios"', {
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
    },],
  ],
  'targets': [
    {
      'target_name': 'libjsoncpp',
      'type': 'static_library',
      'include_dirs': [
        'jsoncpp/include',
      ],
      'all_dependent_settings': {
        'include_dirs': [
          'jsoncpp/include',
        ],
      },
      'sources': [
        'jsoncpp/src/lib_json/json_reader.cpp',
        'jsoncpp/src/lib_json/json_value.cpp',
        'jsoncpp/src/lib_json/json_writer.cpp',
      ],
      'defines': [
        'JSON_USE_EXCEPTION=0',
      ],
    },
  ],
}
