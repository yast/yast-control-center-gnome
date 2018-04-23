FROM yastdevel/cpp:sle12-sp4

RUN zypper --gpg-auto-import-keys --non-interactive in --no-recommends \
  "pkgconfig(gio-unix-2.0)" \
  "pkgconfig(glib-2.0) >= 2.31.0" \
  "pkgconfig(gtk+-3.0)" \
  "pkgconfig(libgnome-menu-3.0)"
COPY . /usr/src/app
