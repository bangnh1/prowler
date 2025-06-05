# User Registration Settings

## ALLOW_SIGNUP

The `ALLOW_SIGNUP` setting controls whether new users can self-register without an invitation.

- When set to `True` (default): Anyone can register a new account
- When set to `False`: Only users with a valid invitation token can register

### Configuration

#### Using environment variables:

```bash
export ALLOW_SIGNUP=False
```

#### In Helm chart (values.yaml):

```yaml
secrets:
  # ...other settings...
  ALLOW_SIGNUP: False
```

### Use Cases

1. **Public Prowler Instance**: Keep `ALLOW_SIGNUP=True` to allow anyone to register
2. **Private Enterprise Deployment**: Set `ALLOW_SIGNUP=False` to require invitations, giving administrators control over who can access the system

### Notes

- When `ALLOW_SIGNUP=False`, the API will return a 400 Bad Request with an appropriate error message if someone attempts to register without an invitation token
- Users with valid invitation tokens can always register, regardless of this setting
