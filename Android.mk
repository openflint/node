#
# Copyright (C) 2013-2014, Infthink (Beijing) Technology Co., Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
LOCAL_PATH:= $(call my-dir)
include $(CLEAR_VARS)
FLING_NODE_PATH := $(LOCAL_PATH)

.PHONY: fling-node
prebuilt: fling-node
fling-node:
	mkdir -p $(TARGET_OUT)/bin
	rm -rf $(TARGET_OUT)/bin/node
	cd $(ANDROID_BUILD_TOP)
	cp -rf $(FLING_NODE_PATH)/fling-node/fling-node $(TARGET_OUT)/bin/node
	chmod +x $(TARGET_OUT)/bin/node
