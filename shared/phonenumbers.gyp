{
  'conditions': [
    ['OS=="ios"', {
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
    },],
  ],
  'conditions': [
    ['OS=="android"', {
      'targets': [
        {
          'target_name': 'phonenumbersprotos',
          'type': 'static_library',
          'includes': [
            '../../clients/shared/protoc.gypi',
          ],
          'dependencies': [
            '../../third_party/shared/protobuf.gyp:libprotobuf',
          ],
          'sources': [
            'phonenumbers/resources/phonemetadata.proto',
            'phonenumbers/resources/phonenumber.proto',
          ],
          'variables': {
            'proto_out_dir': 'phonenumbers/cpp/src/phonenumbers/',
          },
        },
      ],
    },],
  ],
  'targets': [
    {
      'target_name': 'libphonenumbers',
      'type': 'static_library',
      'sources': [
        'phonenumbers/cpp/src/phonenumbers/asyoutypeformatter.cc',
        'phonenumbers/cpp/src/phonenumbers/default_logger.cc',
        'phonenumbers/cpp/src/phonenumbers/lite_metadata.cc',
        'phonenumbers/cpp/src/phonenumbers/logger.cc',
        'phonenumbers/cpp/src/phonenumbers/phonenumber.cc',
        'phonenumbers/cpp/src/phonenumbers/phonenumbermatch.cc',
        'phonenumbers/cpp/src/phonenumbers/phonenumberutil.cc',
        'phonenumbers/cpp/src/phonenumbers/regexp_adapter_re2.cc',
        'phonenumbers/cpp/src/phonenumbers/regexp_cache.cc',
        'phonenumbers/cpp/src/phonenumbers/stringutil.cc',
        'phonenumbers/cpp/src/phonenumbers/unicodestring.cc',

        'phonenumbers/cpp/src/phonenumbers/base/strings/string_piece.cc',
        'phonenumbers/cpp/src/phonenumbers/utf/rune.c',
        'phonenumbers/cpp/src/phonenumbers/utf/unilib.cc',
        'phonenumbers/cpp/src/phonenumbers/utf/unicodetext.cc',
      ],
      'defines': [
        'I18N_PHONENUMBERS_USE_RE2',
      ],
      'include_dirs': [
        '.',
        'phonenumbers/cpp/src',
        '${SHARED_INTERMEDIATE_DIR}',  # for protos
        # HACK HACK:  we've modified phonenumbers to use our Mutex.h,
        # but since gyp sees through symlinks we have to jump through hoops.
        '../../clients/shared',
      ],
      'dependencies': [
        'icu.gyp:icuuc',
        'protobuf.gyp:libprotobuf',
        're2.gyp:libre2',
      ],
      'all_dependent_settings': {
        'include_dirs': [
          'phonenumbers/cpp/src',
        ],
      },
      'conditions': [
        ['OS=="ios"', {
          'sources': [
            'phonenumbers/resources/phonemetadata.proto',
            'phonenumbers/resources/phonenumber.proto',
          ],
          'variables': {
            'proto_out_dir': 'phonenumbers/',
          },
        },],
        ['OS=="android"', {
          'variables': {
            'proto_out_dir': 'phonenumbers/cpp/src/phonenumbers/',
          },
          'dependencies': [
            'phonenumbersprotos',
          ],
          # Gyp-android will not add 'dependencies' to sub-projects, so we need to specify libraries manually.
          'libraries': [
            'third_party_shared_libprotobuf_lite_gyp.a',
            'third_party_shared_libre2_gyp.a',
          ],
        },],
      ],
      'includes': [
        '../../clients/shared/protoc.gypi',
      ],
    },
  ],
}
