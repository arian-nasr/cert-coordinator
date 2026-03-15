test_domain_request = {
    'domain': 'example.com',
    'credentials_file': '.secrets.example/certbot/cloudflare.ini',
    'email': 'admin@example.com'
}

if __name__ == '__main__':
    from schemas import DomainRequest
    from pydantic import ValidationError

    try:
        domain_request = DomainRequest(**test_domain_request)
        print("DomainRequest validation successful:", domain_request)
    except ValidationError as e:
        print("DomainRequest validation failed:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
        raise e