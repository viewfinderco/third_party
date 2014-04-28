{
  'targets': [
    {
      'target_name': 'libfacebook',
      'type': 'static_library',
      'dependencies': [
        'json.gyp:libjson',
      ],
      'sources': [
        'facebook/FBDialog.h',
        'facebook/FBDialog.m',
        'facebook/FBLoginDialog.h',
        'facebook/FBLoginDialog.m',
        'facebook/FBRequest.h',
        'facebook/FBRequest.m',
        'facebook/Facebook.h',
        'facebook/Facebook.m',
      ],
      'include_dirs': [
        'facebook/JSON',
      ],
      'mac_framework_dirs': [
        '${SDKROOT}/System/Library/Frameworks/UIKit.framework',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          'facebook',
        ],
        'mac_bundle_resources': [
          'facebook/FBDialog.bundle',
        ],
      },
    },
  ],
}
