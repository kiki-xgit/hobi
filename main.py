from fasthtml.common import *

css_rules = """
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    background-color: #000000;
    color: #ffffff;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    width: 100vw;
    overflow: hidden;
    padding: 1rem;
}
.content {
    text-align: center;
    width: 100%;
    max-width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
h1 {
    font-size: clamp(2.5rem, 8vw, 4rem);
    font-weight: 800;
    letter-spacing: -0.05em;
    background: linear-gradient(180deg, #ffffff 0%, #a1a1a1 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    line-height: 1.1;
}
.info-container {
    margin-top: 1.5rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1.25rem;
}
.clock-section {
    font-size: 1.1rem;
    font-variant-numeric: tabular-nums;
    color: #999999;
    letter-spacing: 0.05em;
}
.location {
    color: #999999;
    font-size: 0.9rem;
}
.footer {
    font-size: 0.85rem;
    color: #999999;
    letter-spacing: 0.05em;
    font-weight: 400;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
.logo-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 0.75rem;
    width: 100%;
}
.logo-box {
    max-width: clamp(100px, 25vw, 140px);
    height: auto;
}
"""

js_code = """
function updateTime() {
    const now = new Date();
    const utc = now.getTime() + (now.getTimezoneOffset() * 60000);
    const jkt = new Date(utc + (3600000 * 7));
    
    const hours = String(jkt.getHours()).padStart(2, '0');
    const minutes = String(jkt.getMinutes()).padStart(2, '0');
    const seconds = String(jkt.getSeconds()).padStart(2, '0');
    document.getElementById('clock').textContent = `${hours}:${minutes}:${seconds}`;

    const days = ['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu'];
    const dayName = days[jkt.getDay()];
    document.getElementById('day').textContent = dayName + ',';

    const day = String(jkt.getDate()).padStart(2, '0');
    const months = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'];
    const month = months[jkt.getMonth()];
    document.getElementById('date').textContent = `${day} ${month}`;
    
    document.getElementById('year').textContent = jkt.getFullYear();
}
setInterval(updateTime, 1000);
window.addEventListener('load', updateTime);
"""

_app, rt = fast_app(
    db_file=None, 
    live=False,
    hdrs=(
        Style(NotStr(css_rules)),
        Script(NotStr(js_code))
    )
)

@rt("/")
def get():
    return Title("Hello World"), Main(cls="content")(
        H1("Hello World!"),
        Div(cls="info-container")(
            Div(cls="footer")(
                Div(cls="logo-container")(
                    Img(src="vercel-logo.png", cls="logo-box"),
                    Img(src="fasthtml-logo.svg", cls="logo-box")
                )
            ),
            Div(cls="clock-section")(
                Span(id="day"), " ",
                Span(id="date"), " ", 
                Span(id="year"), " ", 
                Span("00:00:00", id="clock"), " ", 
                Span("UTC+7", cls="location")
            )
        )
    )

app = _app

if __name__ == "__main__":
    serve()
