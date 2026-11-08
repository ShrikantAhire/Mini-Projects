"""Ask Gemini to watch a video or listen to audio.

Usage: python3 tools/gemini_watch.py <file.mp4|file.mp3|file.wav> "<question>" [model]

The Gemini key is stored as a network secret on the cloud environment and is
added by the proxy, so no key is needed here. Files are sent inline, so keep
them under about 15 MB (split or compress longer videos with ffmpeg first).
"""
import base64, json, sys, urllib.request, urllib.error, mimetypes

URL = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"

def ask(path, prompt, model="gemini-3.5-flash"):
    data = base64.b64encode(open(path, "rb").read()).decode()
    if path.lower().endswith((".mp3", ".wav")):
        part = {"type": "input_audio", "input_audio": {"data": data, "format": path.rsplit(".", 1)[1].lower()}}
    else:
        mime = mimetypes.guess_type(path)[0] or "video/mp4"
        part = {"type": "image_url", "image_url": {"url": f"data:{mime};base64,{data}"}}
    body = {"model": model, "messages": [{"role": "user", "content": [{"type": "text", "text": prompt}, part]}]}
    req = urllib.request.Request(URL, data=json.dumps(body).encode(), headers={
        "Content-Type": "application/json", "Authorization": "Bearer proxy-injected"})
    try:
        return json.load(urllib.request.urlopen(req, timeout=300))["choices"][0]["message"]["content"]
    except urllib.error.HTTPError as e:
        return f"HTTP {e.code}: {e.read().decode()[:500]}"

if __name__ == "__main__":
    print(ask(sys.argv[1], sys.argv[2], *sys.argv[3:4]))
