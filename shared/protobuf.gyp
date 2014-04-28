{
  'targets': [
    # The "lite" lib is about 1/7th the size of the heavy lib,
    # but it doesn't support some of the more exotic features of
    # protobufs, like reflection.  To generate C++ code that can link
    # against the lite version of the library, add the option line:
    #
    #   option optimize_for = LITE_RUNTIME;
    #
    # to your .proto file.
    {
      'target_name': 'libprotobuf_lite',
      'type': 'static_library',
      'defines': [
        'GOOGLE_PROTOBUF_NO_RTTI',
        'GOOGLE_PROTOBUF_NO_STATIC_INITIALIZER',
      ],
      'all_dependent_settings': {
        'include_dirs': [
          'protobuf/src',
        ],
      },
      'direct_dependent_settings': {
        'defines': [
          'GOOGLE_PROTOBUF_NO_RTTI',
          'GOOGLE_PROTOBUF_NO_STATIC_INITIALIZER',
        ],
      },
      'include_dirs': [
        'protobuf/src',
        'protobuf',
      ],
      'sources': [
        'protobuf/src/google/protobuf/stubs/atomicops.h',
        'protobuf/src/google/protobuf/stubs/atomicops_internals_arm_gcc.h',
        'protobuf/src/google/protobuf/stubs/atomicops_internals_atomicword_compat.h',
        'protobuf/src/google/protobuf/stubs/atomicops_internals_macosx.h',
        'protobuf/src/google/protobuf/stubs/atomicops_internals_mips_gcc.h',
        'protobuf/src/google/protobuf/stubs/atomicops_internals_x86_gcc.cc',
        'protobuf/src/google/protobuf/stubs/atomicops_internals_x86_gcc.h',
        'protobuf/src/google/protobuf/stubs/atomicops_internals_x86_msvc.cc',
        'protobuf/src/google/protobuf/stubs/atomicops_internals_x86_msvc.h',
        'protobuf/src/google/protobuf/stubs/common.h',
        'protobuf/src/google/protobuf/stubs/once.h',
        'protobuf/src/google/protobuf/stubs/platform_macros.h',
        'protobuf/src/google/protobuf/extension_set.h',
        'protobuf/src/google/protobuf/generated_message_util.h',
        'protobuf/src/google/protobuf/message_lite.h',
        'protobuf/src/google/protobuf/repeated_field.h',
        'protobuf/src/google/protobuf/unknown_field_set.cc',
        'protobuf/src/google/protobuf/unknown_field_set.h',
        'protobuf/src/google/protobuf/wire_format_lite.h',
        'protobuf/src/google/protobuf/wire_format_lite_inl.h',
        'protobuf/src/google/protobuf/io/coded_stream.h',
        'protobuf/src/google/protobuf/io/zero_copy_stream.h',
        'protobuf/src/google/protobuf/io/zero_copy_stream_impl_lite.h',
      
        'protobuf/src/google/protobuf/stubs/common.cc',
        'protobuf/src/google/protobuf/stubs/once.cc',
        'protobuf/src/google/protobuf/stubs/hash.h',
        'protobuf/src/google/protobuf/stubs/map-util.h',
        'protobuf/src/google/protobuf/stubs/stl_util-inl.h',
        'protobuf/src/google/protobuf/extension_set.cc',
        'protobuf/src/google/protobuf/generated_message_util.cc',
        'protobuf/src/google/protobuf/message_lite.cc',
        'protobuf/src/google/protobuf/repeated_field.cc',
        'protobuf/src/google/protobuf/wire_format_lite.cc',
        'protobuf/src/google/protobuf/io/coded_stream.cc',
        'protobuf/src/google/protobuf/io/coded_stream_inl.h',
        'protobuf/src/google/protobuf/io/zero_copy_stream.cc',
        'protobuf/src/google/protobuf/io/zero_copy_stream_impl_lite.cc',
        'protobuf/config.h',
      ],
    },
    # This is the full, heavy protobuf lib that's needed for c++ .protos
    # that don't specify the LITE_RUNTIME option.  The protocol
    # compiler itself (protoc) falls into that category.
    {
      'target_name': 'libprotobuf',
      'type': 'static_library',
      'dependencies': [
        'libprotobuf_lite',
      ],
      'include_dirs': [
        'protobuf/src',
        'protobuf',
      ],
      'sources': [
        'protobuf/src/google/protobuf/descriptor.h',
        'protobuf/src/google/protobuf/descriptor.pb.h',
        'protobuf/src/google/protobuf/descriptor_database.h',
        'protobuf/src/google/protobuf/dynamic_message.h',
        'protobuf/src/google/protobuf/generated_enum_reflection.h',
        'protobuf/src/google/protobuf/generated_message_reflection.h',
        'protobuf/src/google/protobuf/message.h',
        'protobuf/src/google/protobuf/reflection_ops.h',
        'protobuf/src/google/protobuf/service.h',
        'protobuf/src/google/protobuf/text_format.h',
        'protobuf/src/google/protobuf/wire_format.h',
        'protobuf/src/google/protobuf/io/gzip_stream.h',
        'protobuf/src/google/protobuf/io/printer.h',
        'protobuf/src/google/protobuf/io/tokenizer.h',
        'protobuf/src/google/protobuf/io/zero_copy_stream_impl.h',
        'protobuf/src/google/protobuf/compiler/code_generator.h',
        'protobuf/src/google/protobuf/compiler/command_line_interface.h',
        'protobuf/src/google/protobuf/compiler/importer.h',
        'protobuf/src/google/protobuf/compiler/java/java_doc_comment.cc',
        'protobuf/src/google/protobuf/compiler/java/java_doc_comment.h',
        'protobuf/src/google/protobuf/compiler/parser.h',
  
        'protobuf/src/google/protobuf/stubs/strutil.cc',
        'protobuf/src/google/protobuf/stubs/strutil.h',
        'protobuf/src/google/protobuf/stubs/substitute.cc',
        'protobuf/src/google/protobuf/stubs/substitute.h',
        'protobuf/src/google/protobuf/stubs/stl_util.h',
        'protobuf/src/google/protobuf/stubs/stringprintf.cc',
        'protobuf/src/google/protobuf/stubs/stringprintf.h',
        'protobuf/src/google/protobuf/stubs/structurally_valid.cc',
        'protobuf/src/google/protobuf/stubs/template_util.h',
        'protobuf/src/google/protobuf/stubs/type_traits.h',
  
        'protobuf/src/google/protobuf/descriptor.cc',
        'protobuf/src/google/protobuf/descriptor.pb.cc',
        'protobuf/src/google/protobuf/descriptor_database.cc',
        'protobuf/src/google/protobuf/dynamic_message.cc',
        'protobuf/src/google/protobuf/extension_set.cc',
        'protobuf/src/google/protobuf/extension_set.h',
        'protobuf/src/google/protobuf/extension_set_heavy.cc',
        'protobuf/src/google/protobuf/generated_message_reflection.cc',
        'protobuf/src/google/protobuf/message.cc',
        'protobuf/src/google/protobuf/reflection_ops.cc',
        'protobuf/src/google/protobuf/service.cc',
        'protobuf/src/google/protobuf/text_format.cc',
        'protobuf/src/google/protobuf/wire_format.cc',
        # This file pulls in zlib, but it's not actually used by protoc, so
        # instead of compiling zlib for the host, let's just exclude this.
        # 'protobuf/src/protobuf/src/google/protobuf/io/gzip_stream.cc',
        'protobuf/src/google/protobuf/io/printer.cc',
        'protobuf/src/google/protobuf/io/tokenizer.cc',
        'protobuf/src/google/protobuf/io/zero_copy_stream_impl.cc',
        'protobuf/src/google/protobuf/compiler/importer.cc',
        'protobuf/src/google/protobuf/compiler/parser.cc',
      ],
    },
  ],
}
