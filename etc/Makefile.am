desktopdir       = $(datadir)/applications
desktop_DATA     = y2cc-gnome.desktop

schemasdir   = @GCONF_SCHEMA_FILE_DIR@
schemas_DATA = y2cc-gnome.schemas

# hacks
menudir = /etc/xdg/menus
menu_DATA = y2cc-gnome.menu

# built from yast2 groups/ desktop files
directorydir = $(datadir)/desktop-directories
directory_DATA = $(wildcard suse-y2cc-gnome-*.directory)

NLD_YAST_THEME_DIR = /usr/share/YaST2/theme/NLD
# clobber the NLD yast2 theme to make it an icon theme
indexdir = $(NLD_YAST_THEME_DIR)/icons
index_DATA = index.theme

$(desktop_DATA): $(desktop_DATA).in
	sed -e "s|\@BINDIR\@|$(bindir)|" $< > $@

$(schemas_DATA): $(schemas_DATA).in
	sed -e "s|\@DATADIR\@|$(datadir)|g" $< > $@

# we also require a symlink creating in the package
link-hicolor:
	mkdir -p $(DESTDIR)$(NLD_YAST_THEME_DIR) ; ln -s icons $(DESTDIR)$(NLD_YAST_THEME_DIR)/hicolor

install-data-local: link-hicolor
	if test -z "$(DESTDIR)" ; then \
		for p in $(schemas_DATA) ; do \
			GCONF_CONFIG_SOURCE=$(GCONF_SCHEMA_CONFIG_SOURCE) $(GCONFTOOL) --makefile-install-rule $$p; \
		done \
	fi

EXTRA_DIST = $(desktop_DATA).in $(schemas_DATA).in $(menu_DATA) $(directory_DATA) $(index_DATA)

CLEANFILES = $(desktop_DATA) $(schemas_DATA)
