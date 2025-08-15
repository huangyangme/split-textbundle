# 把 Ulysses 导出的 TextBundle 拆分成每篇文章单独的 Markdown

想把 Ulysses 的文章**批量**导出为 Markdown（用来备份或迁移），看似简单（Ulysses 自身提供了丰富的导出选项），但只要尝试一下就会发现并非易事。

如果选择导出为 Markdown，我们会得到如下文件结构的文件：

```
/
  ├── index.md
  ├── image1.jpg
  └── image2.jpg
  └── ...
```

`index.md` 是我们选择的所有文章，是的，**Ulysses 会把我们的所有文章变成一个 Markdown 文件，而不是每篇文章一个 Markdown 文件**。

另一种方法是用 Ulysses 导出为 [TextBundle](https://textbundle.org) ，这是**一种打包 Markdown 及其相关资源的文件格式**，由 Ulysses 的开发团队和一些 Markdown 编辑器开发者一起制定，目的就是解决 Markdown 文件传播时内嵌资源（比如图片）丢失的问题。Ulysses、iA Writer、Bear 等编辑器都支持 TextBundle 的文件交换。

TextBundle 文件本质上就是一个压缩打包。用 Ulysses 导出文章合集的 `.textbundle` 文件的默认目录结构如下：

```
xxx.textbundle
  ├── text.md
  ├── info.json
  └── assets/
        ├── image1.jpg
        ├── image2.png
        ├── ...
```

Ulysses 仍会把多篇文章合并成一个 Markdown（这里是 `text.md`），`assets` 目录下是所有图片。

我们可以写一个 Python 脚本把 `text.md` 按照一级标题 # 拆分成多篇 Markdown 文件，并把一级标题作为文件名。

把导出的 `xxx.textbundle` 和 `split_textbundle.py` 这两个文件放在同一个文件夹（比如名叫 `split_output`）内，且目录下只有这两个文件。

```
split_output/
  ├── xxx.textbundle
  ├── split_textbundle.py
```

打开终端，进入文件夹，运行脚本：

```bash
python3 split_textbundle.py
```

脚本会自动生成一个 `split_output` 文件夹，里面包含每篇文章的 Markdown 文件，并复制 `assets` 文件夹。

```
split_output/
  ├── xxx.textbundle
  ├── split_textbundle.py
  ├── split_output
    ├── assets/
    ├── 0001.md
    ├── 0002.md
    ├── 0003.md
    ├── ...
```

现在我们可以把 `split_output` 文件夹里的所有文件——包括 Markdown 文章和图片——备份到别的地方，或者迁移到 Typora、Obsidian 等你喜欢用的其他 Markdown 编辑写作工具。
