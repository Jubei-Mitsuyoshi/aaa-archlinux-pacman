self.description = "do not remove directory symlink if another package has file in its path"

lp1 = pmpkg("pkg1")
lp1.files = ["usr/lib/foo",
             "lib -> usr/lib"]
self.addpkg2db("local", lp1)

lp2 = pmpkg("pkg2")
lp2.files = ["lib/bar"]
self.addpkg2db("local", lp2)

p = pmpkg("pkg1", "1.0-2")
p.files = ["usr/lib/foo"]
self.addpkg2db("sync", p)

self.args = "-S pkg1"

self.addrule("PACMAN_RETCODE=1")
self.addrule("PKG_VERSION=pkg1|1.0-1")
self.addrule("FILE_EXIST=lib/bar")

self.expectfailure = True
