from flask import Flask, Response
import base64
import os

app = Flask(__name__)

# Photo ko app.py ke saath same folder mein anjali.jpg naam se rakho.
PHOTO_PATH = os.path.join(os.path.dirname(__file__), "anjali.jpg")

try:
    with open(PHOTO_PATH, "rb") as photo:
        PHOTO_DATA = base64.b64encode(photo.read()).decode("utf-8")
except FileNotFoundError:
    PHOTO_DATA = ""

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>For My Bebo ❤️</title>

<script type="importmap">
{
  "imports": {
    "three": "https://cdn.jsdelivr.net/npm/three@0.180.0/build/three.module.js"
  }
}
</script>

<style>
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    min-height: 100vh;
    overflow-x: hidden;
    background: #10051c;
    color: white;
    font-family: "Segoe UI", Arial, sans-serif;
}

#universe {
    position: fixed;
    inset: 0;
    width: 100%;
    height: 100%;
    z-index: 0;
}

.glow {
    position: fixed;
    inset: 0;
    z-index: 1;
    pointer-events: none;
    background:
        radial-gradient(circle at 15% 20%,
            rgba(160,60,255,.25), transparent 40%),
        radial-gradient(circle at 85% 75%,
            rgba(255,60,160,.20), transparent 40%);
}

main {
    position: relative;
    z-index: 2;
    max-width: 850px;
    width: calc(100% - 32px);
    margin: auto;
    padding: 45px 0;
    text-align: center;
}

.badge {
    display: inline-block;
    border: 1px solid #ff91ce;
    border-radius: 50px;
    padding: 10px 20px;
    color: #ffd0e9;
    font-size: 11px;
    letter-spacing: 3px;
    animation: appear 1s both;
}

h1 {
    margin-top: 25px;
    font-size: clamp(42px, 8vw, 80px);
    line-height: 1.15;
}

.name {
    display: block;
    color: #ff91cb;
    text-shadow: 0 0 20px #ff399e, 0 0 50px #a44bff;
    animation: glowText 2s infinite alternate;
}

.subtitle {
    max-width: 580px;
    margin: 20px auto;
    color: #ead7f6;
    line-height: 1.9;
}

.heart-scene {
    height: 290px;
    display: grid;
    place-items: center;
    position: relative;
    perspective: 900px;
}

.heart {
    font-size: 115px;
    filter: drop-shadow(0 0 25px #ff329d);
    animation: heartbeat 1.4s infinite;
    transform-style: preserve-3d;
    z-index: 2;
}

.orbit {
    position: absolute;
    width: 210px;
    height: 210px;
    border: 1px solid #ff87cf99;
    border-radius: 50%;
    transform: rotateX(65deg);
    animation: rotate 8s linear infinite;
}

.orbit.two {
    width: 260px;
    height: 260px;
    border-color: #ad71ff99;
    transform: rotateY(65deg);
    animation-duration: 12s;
    animation-direction: reverse;
}

.orbit.three {
    width: 170px;
    height: 170px;
    border-color: #ffffff55;
    transform: rotateY(40deg);
    animation-duration: 6s;
}

.photo-card {
    width: min(330px, 100%);
    margin: 0 auto 40px;
    padding: 11px;
    border-radius: 25px;
    background: linear-gradient(135deg, #ff92d1, #a35bff, #ff48a3);
    background-size: 300% 300%;
    box-shadow: 0 0 40px #ff4ca533, 0 25px 60px #0007;
    transition: transform .15s;
    animation: borderMove 5s infinite;
}

.photo-card img {
    width: 100%;
    height: 390px;
    display: block;
    object-fit: contain;
    background: #24102d;
    border-radius: 17px;
}

.photo-card h2 {
    padding: 18px 0 8px;
    text-shadow: 0 0 15px #ff49a8;
}

.photo-card p {
    padding-bottom: 10px;
    color: #ffe1f3;
    font-size: 13px;
}

.message {
    max-width: 650px;
    margin: auto;
    padding: 27px;
    border: 1px solid #ffb2df44;
    border-radius: 24px;
    background: #ffffff0b;
    backdrop-filter: blur(12px);
    line-height: 1.9;
    color: #f4e4fc;
}

.message h2 {
    margin-bottom: 15px;
    color: #ff9bd2;
}

.message p {
    margin-top: 12px;
}

.buttons {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 12px;
    margin: 28px 0;
}

button {
    border: 1px solid #ffffff22;
    border-radius: 50px;
    padding: 14px 22px;
    color: white;
    cursor: pointer;
    font-size: 14px;
    font-weight: bold;
    transition: .25s;
}

button:hover {
    transform: translateY(-4px) scale(1.04);
}

.primary {
    background: linear-gradient(135deg, #ff419d, #9c4bff);
    box-shadow: 0 8px 25px #ff419d44;
}

.secondary {
    background: #ffffff12;
}

#surprise {
    min-height: 35px;
    margin: 20px auto;
    color: #ffb3dd;
    font-size: 20px;
}

footer {
    margin-top: 30px;
    color: #c4a4d7;
    font-size: 11px;
    letter-spacing: 3px;
}

.modal {
    position: fixed;
    inset: 0;
    z-index: 10;
    display: none;
    align-items: center;
    justify-content: center;
    padding: 18px;
    background: #090013eF;
    backdrop-filter: blur(12px);
}

.modal.open {
    display: flex;
    animation: appear .3s;
}

.letter {
    max-width: 470px;
    width: 100%;
    max-height: 85vh;
    overflow-y: auto;
    padding: 30px 24px;
    text-align: center;
    border: 1px solid #ff9cdb88;
    border-radius: 25px;
    background: linear-gradient(145deg, #4b1855, #190a2b);
    box-shadow: 0 0 55px #ff42a633;
    animation: letterOpen .5s;
}

.letter .rose {
    font-size: 50px;
}

.letter h2 {
    margin: 18px 0;
    color: #ff9bd2;
}

.letter p {
    margin: 14px 0;
    line-height: 1.9;
    color: #f3e1fb;
}

.signature {
    margin: 25px 0;
    color: #ff9bd2;
    line-height: 1.8;
}

.floating {
    position: fixed;
    z-index: 8;
    pointer-events: none;
    animation: fly 2.3s ease-out forwards;
}

@keyframes appear {
    from { opacity: 0; transform: translateY(18px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes glowText {
    from { filter: brightness(.85); }
    to { filter: brightness(1.3); }
}

@keyframes heartbeat {
    0%,100% { transform: scale(1) rotateY(-10deg); }
    50% { transform: scale(1.16) rotateY(10deg); }
}

@keyframes rotate {
    from { rotate: 0deg; }
    to { rotate: 360deg; }
}

@keyframes borderMove {
    0%,100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

@keyframes fly {
    from {
        opacity: 1;
        transform: translateY(0) scale(.5);
    }
    to {
        opacity: 0;
        transform: translate(var(--dx),var(--dy)) scale(1.6) rotate(30deg);
    }
}

@keyframes letterOpen {
    from { opacity: 0; transform: scale(.8) translateY(20px); }
    to { opacity: 1; transform: scale(1) translateY(0); }
}

@media(max-width:600px) {
    main { padding: 35px 0; }
    .heart-scene { height: 255px; }
    .photo-card img { height: 350px; }
    .message { padding: 22px 17px; }
    .buttons button { width: min(100%, 290px); }
}

@media(prefers-reduced-motion:reduce) {
    *, *::before, *::after {
        animation-duration: .01ms !important;
        animation-iteration-count: 1 !important;
    }
}
</style>
</head>

<body>

<canvas id="universe"></canvas>
<div class="glow"></div>

<main>

    <div class="badge">✦ A LITTLE UNIVERSE FOR YOU ✦</div>

    <h1>
        My Favourite
        <span class="name">Anjali ❤️</span>
    </h1>

    <p class="subtitle">
        In a universe full of stars, you will always be my favourite.
        <br>Welcome to your little world, Bebo. 💖
    </p>

    <section class="heart-scene">
        <div class="orbit"></div>
        <div class="orbit two"></div>
        <div class="orbit three"></div>
        <div class="heart">❤️</div>
    </section>

    <section class="photo-card" id="photoCard">
        <img src="data:image/jpeg;base64,PHOTO_PLACEHOLDER"
             alt="Anjali, my Bebo">
        <h2>My Beautiful Bebo 🌹</h2>
        <p>One smile. A thousand beautiful feelings.</p>
    </section>

    <section class="message">
        <h2>Dear Anjali, My Bebo 💗</h2>
        <p>
            If I could give you one thing in life, I would give you
            the ability to see yourself through my eyes.
        </p>
        <p>
            Then you would understand just how special you are
            and why your smile makes my world brighter. ✨
        </p>
    </section>

    <div class="buttons">
        <button class="primary" id="openLetter">
            💌 Open My Heart
        </button>

        <button class="secondary" id="wishButton">
            ✨ Make a Wish
        </button>

        <button class="secondary" id="musicButton">
            🎵 Play Melody
        </button>
    </div>

    <div id="surprise" aria-live="polite"></div>

    <footer>CREATED WITH LOVE BY AKHILESH ❤️</footer>

</main>

<div class="modal" id="modal" role="dialog"
     aria-modal="true" aria-labelledby="letterTitle">

    <div class="letter">
        <div class="rose">🌹💗🌹</div>

        <h2 id="letterTitle">My Dearest Bebo ❤️</h2>

        <p>My sweet Anjali,</p>

        <p>
            I created this little universe just for you because
            I wanted to give you something special.
        </p>

        <p>
            Your smile makes ordinary moments special.
            Your happiness matters to me, and I hope your life
            is filled with kindness, laughter and beautiful memories.
        </p>

        <p>
            No animation can express every feeling, but I hope
            this little surprise reminds you how special you are.
        </p>

        <div class="signature">
            With lots of love,<br>Your Akhilesh ❤️
        </div>

        <button class="primary" id="closeLetter">
            Sending You a Hug 🤗
        </button>
    </div>
</div>

<script type="module">
import * as THREE from "three";

// 3D star universe
const canvas = document.getElementById("universe");

try {
    const scene = new THREE.Scene();

    const camera = new THREE.PerspectiveCamera(
        65, innerWidth / innerHeight, 0.1, 1000
    );

    camera.position.z = 35;

    const renderer = new THREE.WebGLRenderer({
        canvas, alpha: true, antialias: true
    });

    renderer.setPixelRatio(Math.min(devicePixelRatio || 1, 2));
    renderer.setSize(innerWidth, innerHeight);

    const count = 1600;
    const positions = new Float32Array(count * 3);

    for (let i = 0; i < count; i++) {
        positions[i * 3] = (Math.random() - .5) * 100;
        positions[i * 3 + 1] = (Math.random() - .5) * 100;
        positions[i * 3 + 2] = (Math.random() - .5) * 100;
    }

    const geometry = new THREE.BufferGeometry();

    geometry.setAttribute(
        "position",
        new THREE.BufferAttribute(positions, 3)
    );

    const material = new THREE.PointsMaterial({
        color: 0xffb9e5, size: .14,
        transparent: true, opacity: .9
    });

    const stars = new THREE.Points(geometry, material);
    scene.add(stars);

    const particles = [];

    for (let i = 0; i < 60; i++) {
        const particle = new THREE.Mesh(
            new THREE.IcosahedronGeometry(.15, 1),
            new THREE.MeshBasicMaterial({
                color: i % 2 ? 0xff72bd : 0xb16cff,
                wireframe: i % 3 === 0
            })
        );

        particle.position.set(
            (Math.random() - .5) * 50,
            (Math.random() - .5) * 40,
            (Math.random() - .5) * 20
        );

        particle.userData.speed = .003 + Math.random() * .01;

        scene.add(particle);
        particles.push(particle);
    }

    let frame = 0;

    function animate() {
        requestAnimationFrame(animate);
        frame++;

        stars.rotation.y += .0004;
        stars.rotation.x += .0001;

        particles.forEach(p => {
            p.rotation.x += p.userData.speed;
            p.rotation.y += p.userData.speed * 1.3;

            p.position.y += Math.sin(frame * .012) * .003;
        });

        renderer.render(scene, camera);
    }

    animate();

    addEventListener("resize", () => {
        camera.aspect = innerWidth / innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(innerWidth, innerHeight);
    });

    addEventListener("pointermove", e => {
        camera.position.x = (e.clientX / innerWidth - .5) * 2;
        camera.position.y = -(e.clientY / innerHeight - .5) * 2;
        camera.lookAt(0, 0, 0);
    });

} catch (error) {
    console.error("3D error:", error);
}

// Photo's 3D tilt
const photo = document.getElementById("photoCard");

photo.addEventListener("pointermove", e => {
    const r = photo.getBoundingClientRect();

    const x = (e.clientX - r.left) / r.width;
    const y = (e.clientY - r.top) / r.height;

    photo.style.transform =
        `perspective(900px) rotateX(${(0.5-y)*14}deg)
         rotateY(${(x-0.5)*14}deg)`;
});

photo.addEventListener("pointerleave", () => {
    photo.style.transform =
        "perspective(900px) rotateX(0) rotateY(0)";
});

// Floating heart effects
function burst(count = 20) {
    const icons = ["❤️", "💖", "💕", "🌹", "💗", "✨"];

    for (let i = 0; i < count; i++) {
        setTimeout(() => {
            const el = document.createElement("span");

            el.className = "floating";
            el.textContent = icons[Math.floor(Math.random()*icons.length)];

            el.style.left = Math.random()*90 + 5 + "vw";
            el.style.top = Math.random()*60 + 20 + "vh";

            el.style.setProperty("--dx", (Math.random()-.5)*220 + "px");
            el.style.setProperty("--dy", -(100+Math.random()*240) + "px");

            el.style.fontSize = 20 + Math.random()*20 + "px";

            document.body.appendChild(el);

            setTimeout(() => el.remove(), 2400);
        }, i * 40);
    }
}

setTimeout(() => burst(15), 1000);

// Love letter
const modal = document.getElementById("modal");

document.getElementById("openLetter").onclick = () => {
    modal.classList.add("open");
    burst(25);
};

function closeLetter() {
    modal.classList.remove("open");
}

document.getElementById("closeLetter").onclick = closeLetter;

modal.addEventListener("click", e => {
    if (e.target === modal) closeLetter();
});

document.addEventListener("keydown", e => {
    if (e.key === "Escape") closeLetter();
});

// Surprise messages
const messages = [
    "Bebo, your smile is my favourite view. ❤️",
    "A thousand stars, one beautiful Anjali. ✨",
    "Sending you a million virtual hugs! 🤗",
    "You deserve all the happiness in the universe. 💖",
    "This little world was created just for you. 🌹"
];

let messageIndex = 0;

document.getElementById("wishButton").onclick = () => {
    document.getElementById("surprise").textContent =
        messages[messageIndex];

    messageIndex = (messageIndex + 1) % messages.length;
    burst(30);
};

// Original synthesized melody
let audio = null;
let playing = false;
let timer = null;
let noteIndex = 0;

const notes = [
    523.25, 659.25, 783.99, 659.25,
    587.33, 698.46, 880, 783.99,
    659.25, 783.99, 987.77, 880
];

function note(freq) {
    const osc = audio.createOscillator();
    const gain = audio.createGain();

    osc.type = "sine";
    osc.frequency.value = freq;

    const now = audio.currentTime;

    gain.gain.setValueAtTime(.0001, now);
    gain.gain.exponentialRampToValueAtTime(.06, now+.06);
    gain.gain.exponentialRampToValueAtTime(.0001, now+.5);

    osc.connect(gain);
    gain.connect(audio.destination);

    osc.start(now);
    osc.stop(now+.55);
}

function playMelody() {
    if (!playing) return;

    note(notes[noteIndex % notes.length]);
    noteIndex++;

    timer = setTimeout(playMelody, 430);
}

document.getElementById("musicButton").onclick = async () => {
    const button = document.getElementById("musicButton");

    if (playing) {
        playing = false;
        clearTimeout(timer);
        await audio.suspend();
        button.textContent = "🎵 Play Melody";
        return;
    }

    try {
        if (!audio) {
            audio = new (
                window.AudioContext || window.webkitAudioContext
            )();
        }

        await audio.resume();

        playing = true;
        button.textContent = "⏸ Pause Melody";

        playMelody();
    } catch (error) {
        console.error("Audio error:", error);
    }
};
</script>

</body>
</html>
"""


@app.route("/")
def home():
    # Uploaded photo ko isi single-file website mein embed karna.
    page = HTML.replace("PHOTO_PLACEHOLDER", PHOTO_DATA)
    return Response(page, mimetype="text/html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
"""

@app.route("/")
def home():
    page = HTML.replace("PHOTO_PLACEHOLDER", PHOTO_DATA)
    return Response(page, mimetype="text/html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)