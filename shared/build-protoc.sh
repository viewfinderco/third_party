#!/bin/bash

set -e

output_dir=$PWD/bin
OS_NAME=$(uname -s)
BINARY_NAME="${output_dir}/protoc.${OS_NAME}"

PREV_VERSION=""
if [ -e ${BINARY_NAME} ];
then
  PREV_VERSION=$(${BINARY_NAME} --version)
fi

mkdir -p scratch
mkdir -p ${output_dir}

function build_protobuf() {
  pushd scratch
  if ! test -d protobuf; then
    cp -r ../../shared/protobuf/ .
  fi

  pushd protobuf
  ./configure \
    --prefix=${output_dir} \
    --exec-prefix=${output_dir} \
    --disable-shared
  make clean
  make
  popd
  popd
  cp scratch/protobuf/src/protoc ${BINARY_NAME}
}

build_protobuf

CUR_VERSION=""
if [ -e ${BINARY_NAME} ];
then
  CUR_VERSION=$(${BINARY_NAME} --version)
fi

echo "${BINARY_NAME}: ${PREV_VERSION} -> ${CUR_VERSION}"
