# subdomain_enum_tool

A simple Python script to discover live subdomains of any domain using multithreading for faster scanning. This script sends HEAD requests to check the availability of subdomains and saves discovered subdomains to a file.

Features

Reads subdomains from a text file (sub_domain.txt)

Uses HTTPS and HEAD requests for faster response

Supports multithreading for efficient scanning

Saves discovered subdomains to discovered_subdomains.txt

Thread-safe appending using Python threading.Lock()
