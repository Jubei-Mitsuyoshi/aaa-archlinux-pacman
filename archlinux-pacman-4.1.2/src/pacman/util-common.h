/*
 *  util-common.h
 *
 *  Copyright (c) 2006-2013 Pacman Development Team <pacman-dev@archlinux.org>
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#ifndef _PM_UTIL_COMMON_H
#define _PM_UTIL_COMMON_H

const char *mbasename(const char *path);
char *mdirname(const char *path);

#ifndef HAVE_STRNDUP
char *strndup(const char *s, size_t n);
#endif

#endif /* _PM_UTIL_COMMON_H */

/* vim: set ts=2 sw=2 noet: */
