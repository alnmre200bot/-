from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>alnmre200bot - الذكاء الاصطناعي</title>
    <style>
        body { font-family: 'Tajawal', sans-serif; background: #0f172a; color: white; margin: 0; padding: 20px; }
        .chat { max-width: 600px; margin: auto; }
        h1 { text-align: center; color: #38bdf8; }
        .box { background: #1e293b; border-radius: 15px; padding: 15px; height: 400px; overflow-y: auto; margin-bottom: 10px; }
        .msg { margin: 10px 0; padding: 10px; border-radius: 10px; }
        .user { background: #2563eb; text-align: right; }
        .bot { background: #334155; text-align: right; }
        input { width: 75%; padding: 12px; border: none; border-radius: 10px; background: #334155; color: white; }
        button { width: 20%; padding: 12px; border: none; border-radius: 10px; background: #38bdf8; color: #0f172a; font-weight: bold; }
    </style>
</head>
<body>
    <div class="chat">
        <h1>🤖 alnmre200bot</h1>
        <p style="text-align:center">الذكاء الاصطناعي حق محمد النمري</p>
        <div class="box" id="chatbox">
            <div class="msg bot">مرحبا! انا alnmre200bot الذكاء الاصطناعي حقك. اسألني اي شي 👇</div>
        </div>
        <div>
            <input id="msg" placeholder="اكتب سؤالك هنا...">
            <button onclick="send()">ارسل</button>
        </div>
    </div>
<script>
async function send(){
    let m = document.getElementById('msg').value;
    if(!m) return;
    document.getElementById('chatbox').innerHTML += `<div class="msg user">${m}</div>`;
    document.getElementById('msg').value = '';
    let r = await fetch('/ask', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({msg:m})});
    let d = await r.json();
    document.getElementById('chatbox').innerHTML += `<div class="msg bot">${d.reply}</div>`;
    document.getElementById('chatbox').scrollTop = 99999;
}
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/ask', methods=['POST'])
def ask():
    msg = request.json['msg'].lower()
    
    if 'مرحبا' in msg or 'سلام' in msg:
        reply = f"وعليكم السلام! انا alnmre200bot الذكاء الاصطناعي حق محمد النمري. كيف اقدر اخدمك؟"
    elif 'اسمك' in msg:
        reply = "انا alnmre200bot، الذكاء الاصطناعي اللي برمجه محمد النمري خصيصا لك 😎"
    elif 'كيف' in msg:
        reply = "انا بخير دامك بخير يا محمد. جرب تسألني عن اي موضوع: علوم، برمجة، حساب، قصص..."
    else:
        reply = f"سؤال حلو: '{msg}'. انا لسه اتعلم، بس اقدر اجاوبك. جرب تسألني: مرحبا، اسمك، كيف حالك"
    
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
