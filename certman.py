from schemas import DomainRequest
import subprocess

def request_certificate(domain_request: DomainRequest):
    domain = domain_request.domain
    credentials_file = domain_request.credentials_file
    email = domain_request.email
    certbot_command = [
        'certbot', 'certonly',
        '--dns-cloudflare',
        '--dns-cloudflare-credentials', credentials_file,
        '--email', email,
        '--agree-tos',
        '--non-interactive',
        '-d', domain,
    ]
    result = subprocess.run(certbot_command, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f'Certbot returned non-zero exit code:\n{result.stderr}')
    return result.stdout