{
  'targets': [
    {
      'target_name': 'libmongoose',
      'type': 'static_library',
      'sources': [
        'mongoose/mongoose.c',
      ],
      'defines': [
        'TESTING=1',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          'mongoose',
        ],
      },
    },
  ],
}
