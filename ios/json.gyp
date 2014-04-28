{
  'targets': [
     {
      'target_name': 'libjson',
      'type': 'static_library',
      'sources': [
        'facebook/JSON/JSON.h',
        'facebook/JSON/NSObject+SBJSON.m',
        'facebook/JSON/NSString+SBJSON.m',
        'facebook/JSON/SBJSON.m',
        'facebook/JSON/SBJsonBase.m',
        'facebook/JSON/SBJsonParser.m',
        'facebook/JSON/SBJsonWriter.m',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          'facebook/JSON',
        ],
      },
    },
 ],
}
