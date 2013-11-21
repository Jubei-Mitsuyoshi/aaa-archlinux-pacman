self.description = "do not remove directory symlink if incoming package has file in its path (order 1)"

lp = pmpkg("pkg1")
lp.files = ["usr/lib/foo",
            "lib -> usr/lib"]
self.addpkg2db("local", lp)

p1 = pmpkg("pkg1", "1.0-2")
p1.files = ["usr/lib/foo"]
self.addpkg2db("sync", p1)

p2 = pmpkg("pkg2")
p2.files = ["lib/bar"]
self.addpkg2db("sync", p2)

self.args = "-S pkg1 pkg2"

self.addrule("PACMAN_RETCODE=1")
self.addrule("PKG_VERSION=pkg1|1.0-1")
self.addrule("!PKG_EXIST=pkg2")

self.expectfailure = True
