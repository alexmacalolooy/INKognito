
from pyscript import document, ffi
from js import setTimeout

# Keep event callback proxies alive while the page is open.
_callbacks = []

def keep(callback):
    proxy = ffi.create_proxy(callback)
    _callbacks.append(proxy)
    return proxy


# Notification Toast
def show_toast(message):
    toast = document.getElementById("toast")
    toast_message = document.getElementById("toast-message")

    if toast is None or toast_message is None:
        return

    toast_message.textContent = message
    toast.classList.remove("translate-y-32", "opacity-0")
    toast.classList.add("translate-y-0", "opacity-100")

    def hide_toast():
        toast.classList.remove("translate-y-0", "opacity-100")
        toast.classList.add("translate-y-32", "opacity-0")

    setTimeout(keep(hide_toast), 4000)


# Member 4: Mobile Navigation Menu
mobile_button = document.getElementById("mobile-menu-btn")
mobile_menu = document.getElementById("mobile-menu")

if mobile_button is not None and mobile_menu is not None:

    def toggle_mobile_menu(event):
        mobile_menu.classList.toggle("hidden")

        is_open = not mobile_menu.classList.contains("hidden")
        mobile_button.setAttribute("aria-expanded", str(is_open).lower())
        mobile_button.setAttribute(
            "aria-label",
            "Close navigation menu" if is_open else "Open navigation menu"
        )

    mobile_button.addEventListener(
        "click",
        keep(toggle_mobile_menu)
    )

    # Close the mobile menu after selecting a navigation link.
    for link in mobile_menu.querySelectorAll("a"):
        def close_mobile_menu(event):
            mobile_menu.classList.add("hidden")
            mobile_button.setAttribute("aria-expanded", "false")
            mobile_button.setAttribute("aria-label", "Open navigation menu")

        link.addEventListener("click", keep(close_mobile_menu))


# Member 5: Modal Functionality
modal = document.getElementById("simple-modal")
modal_title = document.getElementById("modal-title")

def open_modal(title):
    if modal is None or modal_title is None:
        return

    modal_title.textContent = title
    modal.classList.remove("opacity-0", "pointer-events-none")


def close_modal():
    if modal is None:
        return

    modal.classList.add("opacity-0", "pointer-events-none")


if modal is not None and modal_title is not None:

    # Open the modal when a data-modal element is clicked.
    for element in document.querySelectorAll("[data-modal]"):
        title = element.getAttribute("data-modal")

        element.addEventListener(
            "click",
            keep(lambda event, title=title: open_modal(title))
        )

    # Close the modal using the Close button.
    for element in document.querySelectorAll('[data-action="close-modal"]'):
        element.addEventListener(
            "click",
            keep(lambda event: close_modal())
        )

    # Close the modal when the dark backdrop is clicked.
    def close_if_backdrop(event):
        if event.target == modal:
            close_modal()

    modal.addEventListener(
        "click",
        keep(close_if_backdrop)
    )

    # Close the modal when Escape is pressed.
    def close_on_escape(event):
        if event.key == "Escape":
            close_modal()

    document.addEventListener(
        "keydown",
        keep(close_on_escape)
    )


# Member 6: Newsletter and Notifications
newsletter_email = document.getElementById("newsletter-email")

if newsletter_email is not None:
    newsletter_form = newsletter_email.closest("form")

    if newsletter_form is not None:

        def handle_newsletter(event):
            event.preventDefault()

            email = newsletter_email.value.strip()

            if not email:
                show_toast("Please enter your email address.")
                return

            show_toast("Thank you for subscribing to our newsletter!")
            newsletter_form.reset()

        newsletter_form.addEventListener(
            "submit",
            keep(handle_newsletter)
        )
