from fasthtml.common import *
from fastapi.staticfiles import StaticFiles
from styles import styles
from cards import MENTOR_CARDS

app, rt = fast_app()

# Serve static files
app.mount("/img", StaticFiles(directory="img"), name="img")
app.mount("/pdf", StaticFiles(directory="pdf"), name="pdf")

def render_head(title):
    """Render the <head> section with dynamic title and favicon."""
    return Head(
        Title(title),
        Link(rel="icon", href="/img/favicon.ico?v=2"),
        Meta(charset="UTF-8"),
        Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
    )

def render_footer():
    """Render the footer section."""
    return Div(
        Div(
            Div(
                P(
                    "A project by ",
                    A("Illawarra Multicultural Services", href="https://ims.org.au/", target="_blank"),
                ),
                _style="text-align: center; margin: 10px 0;"
            ),
            Div(
                P(
                    "Web Development by ",
                    A("Code.Sydney", href="https://www.code.sydney/", target="_blank"),
                ),
                P("© 2025 Illawarra Multicultural Services. All rights reserved."),
                _style="text-align: center; margin: 10px 0; font-size: small; color: gray;"
            ),
            _style="background-color: #f8f9fa; padding: 20px; border-top: 1px solid #ddd;"
        )
    )

def render_header():
    """Render the consistent header across pages."""
    return Div(
        Div(
            A(
                Img(src="/img/migramlogo.png", alt="IMS Logo", _style="width: 225px; margin-bottom: 10px;"),
                _style="text-align: center;",
                href="https://www.migram.au",
                target="_blank"
            )
        ),        
        #H1("MIGRAM", _style="text-align: center; margin-bottom: 10px; font-size: 3rem;"),
        P("Empowering migrants of refugee background to thrive and build inclusive communities.", _style="text-align: center; margin-bottom: 10px;"),
        Div(
            A(
                Img(src="/img/imslogo.png", alt="IMS Logo", _style="width: 300px; margin-bottom: 10px;"),
                _style="text-align: center;",
                href="https://ims.org.au/",
                target="_blank"
            )
        ),
        _style="text-align: center; font-family: Arial, sans-serif;"
    )

def render_page(custom_body):
    """Render a page with a consistent header and dynamic body."""
    return Body(
        Div(
            styles,
            render_header(),
            custom_body,
        ),
        _style="font-family: Arial, sans-serif; margin: 40px;"
    )

def render_navbar():
    """Render the burger menu for navigation."""
    return Div(
        Div(
            Div("☰", _class="burger-icon"),
            Div(
                A("Home", href="/", _class="menu-item", _style="display: block; padding: 10px 20px; font-family: Arial;"),
                A("About", href="/about", _class="menu-item", _style="display: block; padding: 10px 20px; font-family: Arial;"),
                _class="menu-content",
                _style="display: none; position: absolute; top: 40px; right: 0; background-color: white; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); z-index: 999;"
            ),
            _style="position: relative;"
        ),
        Script("""
        const burgerIcon = document.querySelector('.burger-icon');
        const menuContent = document.querySelector('.menu-content');

        burgerIcon.addEventListener('click', () => {
            menuContent.style.display = menuContent.style.display === 'block' ? 'none' : 'block';
        });

        window.addEventListener('click', (event) => {
            if (!event.target.matches('.burger-icon')) {
                menuContent.style.display = 'none';
            }
        });
        """),
        _style="position: fixed; top: 10px; right: 10px; padding: 10px; background-color: #f8f9fa; border-radius: 5px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); z-index: 1000;"
    )

@rt("/")
def get(req):
    return Html(
        render_head("Migram - Home"),
        render_navbar(),
        render_page(
            Div(
                Div(
                    Input(_type="text", _placeholder="Search mentors...", _id="search-input", _style="padding: 10px; width: 300px;"),
                    _style="text-align: center; margin: 20px;"
                ),
                Div(
                    *MENTOR_CARDS,
                    _id="portfolio-container",
                    _style="display: flex; flex-wrap: wrap; justify-content: center;"
                ),
                Script("""
                document.getElementById('search-input').addEventListener('input', function() {
                    const query = this.value.toLowerCase();
                    const cards = document.querySelectorAll('.card');

                    cards.forEach(card => {
                        const title = card.querySelector('.card-title').textContent.toLowerCase();
                        const description = card.querySelector('.card-description').textContent.toLowerCase();
                        const isMatch = title.includes(query) || description.includes(query);
                        card.style.display = isMatch ? 'block' : 'none';
                    });
                });
                """),
            )
        ),
        render_footer()
    )

@rt("/about")
def about(req):
    return Html(
        render_head("Migram - About"),
        render_navbar(),
        render_page(
            Div(
                H2("About Us", _style="text-align: center; margin-bottom: 20px;"),
                P(
                    "Migram is a dedicated platform designed to connect migrants from refugee backgrounds with opportunities for low-skilled work. The aim is to help them integrate into their local communities, fostering meaningful connections and participation. At the same time, Migram serves as a way for local communities to support these individuals, creating a network of mutual benefit and empowerment. By bridging the gap, Migram not only provides economic opportunities but also builds a foundation for stronger, more inclusive communities.",
                    _style="text-align: center; font-family: Arial, sans-serif; margin: 20px;"
                ),
            )
        ),
        render_footer()
    )

serve()
