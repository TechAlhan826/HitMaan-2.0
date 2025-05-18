# 🚀 HitMaan 2.0 – Your Terminal API Buddy

Postman? GUI? Nope.
Welcome to `hitmaan`, a fully terminal-driven, human-first API testing CLI built by [@TechAlhan826](https://github.com/TechAlhan826).
Lightweight. Interactive. Hacker-friendly. No bloat. No bulls\*\*t.

---

## 🌟 What is hitmaan?

`hitmaan` is your go-to CLI tool to test REST APIs straight from the terminal.
Send `GET`, `POST`, `PUT`, `DELETE` requests. Add headers, form data, or raw JSON payloads. Get neat, colorful responses.
Feels like Linux. Works like Postman. Built with pure Python + `rich`.

---

## 🔧 Requirements

Make sure you’ve got:

* Python ≥ 3.8
* pip (Python package manager)

Then just:

```bash
pip install requests rich
```

---

## 📦 How to Run

```bash
python hitmaan.py
```

Follow the prompts:

* Select HTTP method
* Paste the URL
* Add headers (as JSON)
* Choose between JSON body or form-data
* View response (status, headers, pretty-printed body)

---

## 🎮 Demo

```bash
$ python hitmaan.py

 —🔥 hitmaan - Your Terminal API Buddy 🔥—
Developed by Alhan ✦ Inspired by FOSS ✦ Just Pure Python Swag

Choose HTTP Method [GET, POST, PUT, DELETE]: POST
Enter full URL: https://jsonplaceholder.typicode.com/posts
Enter Headers as JSON: {"Content-Type": "application/json"}
Do you want to send form-data instead of raw JSON?: No
Enter Request Body as JSON: {"title": "alhan", "body": "vibe", "userId": 17}

👌 Status: 201

📩 Headers:
Key             | Value
----------------|------------------
Content-Type    | application/json; charset=utf-8
...

📟 Response:
{
  "title": "alhan",
  "body": "vibe",
  "userId": 17,
  "id": 101
}
```

---

## ⚙️ Features

* 🌐 Supports **GET, POST, PUT, DELETE**
* 🧠 Smart input prompts with validation
* 📟 Send **JSON body** or **form-data**
* 💫 Colorful UI powered by `rich`
* 💡 Human-friendly errors, raw or JSON body display
* 🪜 No noise, just clean terminal output

---

## 🥪 Use Cases

* Fast API endpoint testing
* Scripting automation with pipes
* Low-resource dev environments
* Terminal lovers who hate mouse-based UIs

---

## 🔐 Future Scope

* Add saved API profiles (like Postman collections)
* Support for file uploads, auth tokens, bearer headers
* Response export to `.json` / `.txt`
* `--headless` mode for non-interactive scripts

---

## 🧠 Behind the Code

Check out the [source code here](./hitmaan.py).
Style inspired by [@TechAlhan826's](https://github.com/TechAlhan826) earlier Python scripting submissions.
All logic, inputs, and output formats crafted to vibe like *you’re hacking something real*.

---

## 🤝 Contribute

PRs welcome from real ones only.
Fork → Clone → Hack it → Send PR.
No plagiarism. No AI junk. Pure dev brain juice only.

---

## 📨 Contact

For any issues, ideas, or features, hit up:
🌐 [https://techyalhan.in](https://techyalhan.in)

---
