include $(TOPDIR)/rules.mk

# Name, version and release number
# The name and version of your package are used to define the variable to point to the build directory of your package: $(PKG_BUILD_DIR)
PKG_NAME:=lidar
PKG_VERSION:=1.0
PKG_RELEASE:=1

# Source settings (i.e. where to find the source codes)
# This is a custom variable, used below
SOURCE_DIR:=./src

PKG_BUILD_DIR := $(BUILD_DIR)/$(PKG_NAME)
include $(INCLUDE_DIR)/package.mk

# Package definition; instructs on how and where our package will appear in the overall configuration menu ('make menuconfig')
define Package/$(PKG_NAME)
  SECTION:=project
  CATEGORY:=Examples
  TITLE:=Lidar
  DEPENDS:=+libc +librt
endef

define Build/Configure
endef

# Package build instructions; invoke the target-specific compiler to first compile the source file, and then to link the file into the final executable
define Build/Compile
	$(MAKE) -C $(PKG_BUILD_DIR) \
			CC="$(TARGET_CC)" \
			CFLAGS="$(TARGET_CFLAGS) -Wall" \
			LDFLAGS="$(TARGET_LDFLAGS)"
endef

# Package install instructions; create a directory inside the package to hold our executable, and then copy the executable we built previously into the folder
define Package/$(PKG_NAME)/install
	$(INSTALL_DIR) $(1)/usr/bin
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/main $(1)/usr/bin
endef

# This command is always the last, it uses the definitions and variables we give above in order to get the job done
$(eval $(call BuildPackage,$(PKG_NAME)))

