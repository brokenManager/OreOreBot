# はらちょヘルプ.md

# 機能一覧
- 時報系 (lib/time_signal.py) にて処理 いっそう追記頼む
  -  指定された時間にmessages.jsonに書いてあるメッセージを送信する
  -  19時、6時に明日、今日の天気を取得して送信する
- 生のメッセージに反応する系 (message_command.py) にて処理
  - 「いっそう」が含まれるメッセージを検出したとき、いっそうの絵文字を送信する
  - 「ハラショー」が含まれるメッセージを検出したとき、はらちょの絵文字を送信する
  - 「疲れた」が含まれるメッセージを検出したとき、特定のメッセージを送信する
  - 「おやすみ」が含まれるメッセージを検出したとき、特定のメッセージを送信する
- GitHub系 (message_command.github) にて処理 いっそう追記頼む
  - 「#」から始まるメッセージを検出したとき、該当するGitHubのリポジトリのtop/issue/pull-requestsのリンクを張る
  -  指定したリポジトリからランダムなissueをみつけて送信する
  -  省略形:
     - "t": "top",
     - "i": "issues",
     - "pr": "pull",
     -  "p": "pull"
  -  特に指定がない場合、brokenManagerから拾ってくる、ただし別のリポジトリを指定することもできる
  -  そのときは「他の鎮守府から...」というメッセージを追加して送信する
  -  例:#OreOreBot/i → https://github.com/brokenManager/OreOreBot/issues をメッセージとともに送信
- 特殊系
  - typoカウンター *だカス というメッセージを検出した場合、そのユーザーごとに*を内部的に保持する
  - 草カウンター 文章中に「草」を検出した場合、そのユーザーの「草」の回数を記録する
- !コマンド系
  - !lol そのユーザーが「草」と発言したを送信する
  - !typo そのユーザーの記録されたtypoを送信する
  - !jd / !judge はらちょオンラインジャッジメントシステム ABC風にジャッジみたいなことをする
    - コマンドの形式は[ここを参照](https://github.com/brokenManager/OreOreBot/pull/68#issuecomment-605038105)
- システム的な機能
  - Bot(中身は人間)の処理を通す機能
  - ~~JSONメッセージをうまく扱うためのクラス、Pythonのstr.format機能{}に対応 使い方は~~ ```instance.get_message()```
  - ↑もしかして消えてる？
- 注釈
  - 各機能はクラスごとに分けられており、シングルトンを継承している