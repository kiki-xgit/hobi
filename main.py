from fasthtml.common import *

_app, rt = fast_app(db_file=None)

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
    margin-top: clamp(4rem, 15vh, 8rem);
}
.clock-section {
    font-size: 1.1rem;
    font-variant-numeric: tabular-nums;
    color: #999999;
    letter-spacing: 0.05em;
    margin-bottom: 1.25rem;
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
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
}
.badge {
    background-color: #ffffff;
    color: #000000;
    padding: 0.3rem 0.7rem;
    border-radius: 20px;
    font-weight: 600;
    display: inline-block;
    animation: badgeGlow 2s ease-in-out infinite alternate;
}
@keyframes badgeGlow {
    from {
        box-shadow: 0 0 8px rgba(255, 255, 255, 0.3), 0 0 15px rgba(255, 255, 255, 0.2);
    }
    to {
        box-shadow: 0 0 18px rgba(255, 255, 255, 0.9), 0 0 28px rgba(255, 255, 255, 0.5);
    }
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

    const day = String(jkt.getDate()).padStart(2, '0');
    const months = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'];
    const month = months[jkt.getMonth()];
    document.getElementById('date').textContent = `${day} ${month}`;
    
    document.getElementById('year').textContent = jkt.getFullYear() + " ";
}

setInterval(updateTime, 1000);
updateTime();
"""

@rt("/")
def get():
    return Title("Hello World"), Html(lang="id")(
        Style(NotStr(css_rules)),
        Body(
            Div(cls="content")(
                H1("Hello World!"),
                Div(cls="info-container")(
                    Div(cls="clock-section")(
                        Span(id="date"), " ", 
                        Span("00:00:00", id="clock"), " ", 
                        Span("Jakarta (UTC+7)", cls="location")
                    ),
                    Div(cls="footer")(
                        Span(id="year"), 
                        " Powered by ", 
                        Span("Vercel Hosting", cls="badge")
                    )
                )
            ),
            Script(NotStr(js_code))
        )
    )

app = _app

if __name__ == "__main__":
    serve()
