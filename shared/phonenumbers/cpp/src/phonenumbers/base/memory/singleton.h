// Copyright (C) 2011 The Libphonenumber Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Author: Philippe Liard

#ifndef I18N_PHONENUMBERS_BASE_SINGLETON_H_
#define I18N_PHONENUMBERS_BASE_SINGLETON_H_

#include <pthread.h>
#include "phonenumbers/base/memory/scoped_ptr.h"

namespace i18n {
namespace phonenumbers {

template <class T>
class Singleton {
 public:
  virtual ~Singleton() {}

  static T* GetInstance() {
    pthread_once(&flag, &Init);
    return instance.get();
  }

 private:
  static void Init() {
    instance.reset(new T());
  }

  static scoped_ptr<T> instance;
  static pthread_once_t flag;
};

template <class T> scoped_ptr<T> Singleton<T>::instance;
template <class T> pthread_once_t Singleton<T>::flag = PTHREAD_ONCE_INIT;

}  // namespace phonenumbers
}  // namespace i18n

#endif // I18N_PHONENUMBERS_BASE_SINGLETON_H_
