#!/usr/bin/env bash

. /usr/share/makepkg/util/message.sh

VERSION=$(uname -r)

if [[ -z "${VERSION}" ]]; then
    error "Could not get the running kernel version number"
    exit 1
elif [[ -s "/usr/lib/modules/backup_${VERSION}.tar.gz" ]]; then
    warning "/usr/lib/modules/backup_${VERSION}.tar.gz already exists: skipping"
elif [[ -d "/usr/lib/modules/${VERSION}" ]]; then
    msg "Creating /usr/lib/modules/backup_${VERSION}.tar.gz"
    cd /usr/lib/modules
    tar czf "backup_${VERSION}.tar.gz" "${VERSION}"
    msg "Removing other backups"
    find . -\( -type f -and -name 'backup_*.tar.gz' \
         -and -not -name "backup_${VERSION}.tar.gz" -\) \
         -delete
else
    warning "/usr/lib/modules/${VERSION} doesn't exist: skipping"
fi
