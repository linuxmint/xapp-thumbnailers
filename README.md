XApp Thumbnailers
-----------------

A collection of thumbnail generators.

Like all XApp projects, this is compatible with all Linux distributions and open to all Gtk desktop environments.

All file managers which are compatible with `/usr/share/thumbnailers` thumbnailers are supported:

- [Caja (MATE)](https://github.com/mate-desktop/caja)
- [Nautilus (GNOME)](https://gitlab.gnome.org/GNOME/nautilus)
- [Nemo (Cinnamon)](https://github.com/linuxmint/nemo)
- [PCManFM (LXDE)](https://github.com/lxde/pcmanfm)
- [Thunar (Xfce)](https://gitlab.xfce.org/xfce/thunar)

So far the following file types are supported:

- **AppImage** (compressed as squashfs, with an icon linked from `.DirIcon`)
- **ePub** (compressed as ZIP, with a cover specified as a `cover-image` property, or a `cover` meta tag).
- **MP3** (with album art specified in their ID3 images tag)
- **RAW** (compatible with dcraw)
