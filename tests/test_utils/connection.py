# -*- coding: utf-8 -*-
import socket


def has_internet_connection():
    """Checks if the system has an internet connection

    Returns:
        bool: True if system has internet connection, False otherwise
    """
    try:
        socket.create_connection(
            ("www.google.com", 80),
            10
        )
        return True
    except Exception:
        return False
