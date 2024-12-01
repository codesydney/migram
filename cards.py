from fasthtml.common import A, Div, H3, Img, P, Style

def generate_linkedin_link(linkedin_link, margin_top="0"):
    """Generate LinkedIn link with an icon."""
    return A(
        Img(
            src="img/linkedin-icon.svg",
            alt="LinkedIn",
            _class="linkedin-icon",
            style=f"margin-top: {margin_top};"  # Control the top margin dynamically
        ),
        href=linkedin_link,
        target="_blank",
        _class="linkedin-link"
    )

def generate_portfolio_link(portfolio_link, icon_size=None):
    """Generate portfolio link with a project icon."""
    return A(
        Img(
            src="img/project-icon.png",
            alt="Project",
            _class="portfolio-icon",
            style=f"width: {icon_size}px; height: {icon_size}px;" if icon_size else ""
        ),
        href=portfolio_link,
        target="_blank",
        _class="portfolio-link"
    )

def generate_booking_button(booking_link, margin_bottom="10px"):
    """Generate a booking button with controllable margin."""
    return A(
        "Book Now",
        href=booking_link,
        target="_blank",
        _class="booking-button",
        style=f"margin-bottom: {margin_bottom};"
    )

def card_3d(
    title, background, line1, line2, line3, link, show_booking=True, 
    booking_link="", is_portfolio=False, icon_size=None, 
    button_margin_bottom="5px", space_between_button_and_icon="5px"
):
    """Generate a 3D card component with mentor or portfolio details."""
    card_body = [
        H3(line1, _class="card-title"),
        P(line2, _class="card-description"),
        P(line3, _class="card-description-small"),
    ]
    if show_booking and not is_portfolio:
        # Add the booking button with dynamic margin
        card_body.append(generate_booking_button(booking_link, margin_bottom=button_margin_bottom))
    
    if is_portfolio:
        card_body.append(generate_portfolio_link(link, icon_size))
    else:
        # Pass space_between_button_and_icon as the margin_top for LinkedIn
        card_body.append(generate_linkedin_link(link, margin_top=space_between_button_and_icon))

    return Div(
        Div(
            Div(
                _style=f"""
                    background-image: url('{background}');
                    width: 600px;
                    height: 450px;
                """,
                _class="card-image"
            ),
            Div(
                *card_body,
                _class="card-content"
            ),
            _class="card-content",
        ),
        _class="card",
        _style="perspective: 1000px; margin: 20px;",
        _data_title=title,
        _data_description=line1,
        _data_description2=line2
    )

MENTOR_CARDS = [
    card_3d(
        "Mentor 1 | ",
        "img/DM-Engramar.png",
        "Engramar Bollas",
        "Basic Python Mentor ($0 per hour)",
        "Guidance on Python for Everybody Course by Prof. Charles Severance",
        "https://linkedin.com/in/engramarbollas",
        show_booking=True,
        booking_link="https://koalendar.com/e/meet-with-code-sydney",
        button_margin_bottom="1px",  # Space below the button
        space_between_button_and_icon="1px"  # Reduced space between button and LinkedIn icon
    )
]

PORTFOLIO_CARDS = [

]
