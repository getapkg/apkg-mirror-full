# aPKG Mirror (Full)
A features-full aPKG mirror with with a web-panel
---
## How to install
aPKG full mirror can be installed either manually or using Docker(recommended)

### Docker
To use aPKG the docker version of the mirror, you need to have docker installed,
how to do that you can find on https://www.docker.com/

If you already have docker installed, run:
```bash
docker pull getapkg/apkg-mirror-full
docker run getapkg/apkg-mirror-full
```
**Done!**

### Manually
To install aPKG manually, you need to have Ubuntu Server 24.04 running.
If you already have Ubuntu Server 24.04, run:
```bash
sudo apt update
sudo apt install python3 python3-pip git

git clone https://github.com/getapkg/apkg-mirror-full.git
cd apkg-mirror-full

python3 -m venv .venv
source .venv/bin/activate

./start.sh
```

**Done!**

---
## How to publish packages?
To publish a package to your new aPKG mirror,
you need to get the source code of your package and make a compile.sh in the root of the source code.
Example compile.sh:
```bash
make -j$(nproc)
make install
```
After you made your compile.sh, you need to archive the source code into (name).zip(not the folder, the code)
and put it into /releases/ on your server
P.S. you dont need to remove the 0.1 folder, please leave it alone.

Then you just go to packages.json in the mirror's root and add your package to it.
**Done**

---
## I found a bug
If you found a bug in aPKG's mirror, please go to https://github.com/getapkg/apkg-mirror-full/issues
and open a new issue.

You need to have a github account to do this.
****
