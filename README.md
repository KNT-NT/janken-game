# じゃんけんゲーム

Pythonで作った、簡単なじゃんけんゲームです。  
グー（G）、チョキ（C）、パー（P）を使って、2本先取の勝負を行います。

---

## 📝 特徴

 listによる手の管理 → `['G', 'C', 'P']`
 dictによる勝敗マップ → `{'G': 'C', 'C': 'P', 'P': 'G'}`
 `random.choice()` による相手の手のランダム化
 `try-except` による入力バリデーション（例外処理）
 `while`ループで2本先取の試合を制御
