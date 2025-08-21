# 双机Git 管理规范

## 1️⃣ 早上开始（新建当天草稿分支）

```bash
git checkout master
git pull
git checkout -b draft-YYYYMMDD
```

------

## 2️⃣ 白天写笔记（随时保存 & 切换电脑）

📍 在任意电脑：

```bash
git add .
git commit -m "WIP: 写到哪儿了"
git push
```

> 第一次创建分支push需要
>
> ```bash
> git push --set-upstream origin draft_821
> ```

📍 在另一台电脑接着写：

```bash
git fetch
git checkout draft-YYYYMMDD
git pull
# 继续写...
```

👉 来回切换 A ↔ B 都重复这个步骤就行。

------

## 3️⃣ 晚上收工（合并当天所有提交）

在任意电脑：

```bash
git checkout master
git merge --squash draft-YYYYMMDD
git commit -m "YYYY-MM-DD 笔记更新"
git push
```

------

## 4️⃣ 清理草稿分支（可选）

如果不想保留当天过程：

```bash
git branch -D draft-YYYYMMDD
git push origin --delete draft-YYYYMMDD
```

------

## ✅ 日志效果（master）

```
2025-08-20 笔记更新
2025-08-21 笔记更新
2025-08-22 笔记更新
...
```

------

这样就能保证：

- **两台电脑随时切换**：只要 `git push` + `git pull`。
- **master 分支干净整洁**：每天只有一个最终提交。
- **是否保留过程自己决定**：留着 draft 分支就有完整细节，删掉就只有整理后的内容。

------



工具：[PDF补丁](https://www.cnblogs.com/pdfpatcher)

自动生成书签

