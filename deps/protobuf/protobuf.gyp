{
  'target_defaults': {
    'conditions': [
      ['OS!="win"', {
        'defines': [
          '_DARWIN_USE_64_BIT_INODE=1',
          '_LARGEFILE_SOURCE',
          '_FILE_OFFSET_BITS=64',
          '_GNU_SOURCE'
        ]
      }],
      ['OS=="solaris"', {
        'defines': [
          '__EXTENSIONS__',
          '_XOPEN_SOURCE=500'
        ]
      }]
    ]
  },

  'targets': [
    {
      'target_name': 'protobuf',
      'type': '<(library)',
      'include_dirs': [ 'include', 'src' ],
      'direct_dependent_settings': {
        'include_dirs': [ 'include' ]
      },
      'defines': [ 'HAVE_CONFIG_H', 'GOOGLE_PROTOBUF_NO_RTTI' ],
      'sources': [
        'common.gypi',
        'src/google/protobuf/text_format.cc',
        'src/google/protobuf/stubs/common.cc',
        'src/google/protobuf/descriptor.cc',
        'src/google/protobuf/descriptor.pb.cc',
        'src/google/protobuf/descriptor_database.cc',
        'src/google/protobuf/reflection_ops.cc',
        'src/google/protobuf/message.cc',
        'src/google/protobuf/message_lite.cc',
        'src/google/protobuf/wire_format.cc',
        'src/google/protobuf/wire_format_lite.cc',
        'src/google/protobuf/unknown_field_set.cc',
        'src/google/protobuf/extension_set.cc',
        'src/google/protobuf/extension_set_heavy.cc',
        'src/google/protobuf/dynamic_message.cc',
        'src/google/protobuf/generated_message_reflection.cc',
        'src/google/protobuf/generated_message_util.cc',
        'src/google/protobuf/repeated_field.cc',
        'src/google/protobuf/io/tokenizer.cc',
        'src/google/protobuf/io/coded_stream.cc',
        'src/google/protobuf/io/zero_copy_stream.cc',
        'src/google/protobuf/io/zero_copy_stream_impl.cc',
        'src/google/protobuf/io/zero_copy_stream_impl_lite.cc',
        'src/google/protobuf/stubs/strutil.cc',
        'src/google/protobuf/stubs/stringprintf.cc',
        'src/google/protobuf/stubs/substitute.cc',
        'src/google/protobuf/stubs/once.cc',
        'src/google/protobuf/stubs/structurally_valid.cc',
        'src/google/protobuf/stubs/atomicops_internals_x86_gcc.cc',
      ],
      'conditions': [
        [ 'library=="static_library"', {
          'defines': [ 'PROTOBUF_STATICLIB' ]
        }, {
          'defines': [ 'PROTOBUF_BUILDING_LIBRARY' ]
        }],
        [ 'OS=="win"', {
        }, {
          # Not Windows i.e. POSIX
          'cflags': [
            '-g',
            '-pedantic',
            '-Wall',
            '-Wextra',
            '-Wno-unused-parameter'
          ],
        }],
        [ 'OS not in "win android"', {
          'cflags': [
            '--std=gnu89'
          ],
        }],
        [ 'OS=="linux"', {
        }],
        [ 'OS=="mac"', {
        }],
        [ 'OS=="freebsd" or OS=="dragonflybsd"', {
        }],
        [ 'OS=="openbsd"', {
        }],
        [ 'OS=="android"', {
        }],
        [ 'OS=="solaris"', {
        }]
      ]
    }
  ]
}
