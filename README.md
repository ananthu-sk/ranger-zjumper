# Ranger & z

This plugin integrates [z](https://github.com/rupa/z) with [ranger](https://github.com/ranger/ranger). It uses the `.z` database to enable quick directory jumping inside ranger. You can watch a demo in this [screencast](https://youtu.be/ciHHbFtz4N8).

> **Note:**
> This branch supports only [z](https://github.com/rupa/z).
> If you want to use [zsh-z](https://github.com/agkozak/zsh-z), see the [master branch](https://github.com/ask1234560/ranger-zjumper/tree/master).

---

## Requirements

* Set the `_Z_SRC` environment variable to the path of `z.sh`.

---

## Installation

```bash
cd "${XDG_CONFIG_HOME:-$HOME/.config}/ranger/plugins"
git clone https://github.com/ask1234560/ranger-zjumper.git

echo -e "# z jumper\nmap cz console z%space" >> "${XDG_CONFIG_HOME:-$HOME/.config}"/ranger/rc.conf
```

Restart ranger after installation.

---

## Usage

* Run `:z dir` to jump to directory.
* Alternatively:
  * Press `c`, then `z`, then type your directory query.

---

## Updating

To update the plugin:

```bash
cd "${XDG_CONFIG_HOME:-$HOME/.config}/ranger/plugins/ranger-zjumper"
git pull
```

---

## See Also

* [ranger-zoxide](https://github.com/jchook/ranger-zoxide/tree/master)

