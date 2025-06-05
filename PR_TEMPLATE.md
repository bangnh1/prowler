# Disable User Registration Feature

This PR adds the ability to disable self-registration in the Prowler API, preventing new users from signing up without invitation.

## Changes

- Added a new configuration setting `ALLOW_SIGNUP` (default: `True`) in Django settings
- Modified the `UserViewSet.create` method to check this setting before allowing user registration
- Updated the Helm chart values to include this new configuration option
- Updated documentation to describe this feature

## Usage

To disable user sign-ups, set `ALLOW_SIGNUP: False` in your deployment configuration:

### For Helm deployments:

```yaml
secrets:
  # ...other settings...
  ALLOW_SIGNUP: False  # This will disable self-registration
```

When sign-ups are disabled:
- Users can only register with valid invitation tokens
- Attempts to register without an invitation will receive a validation error message

## Security Impact

This feature enhances security by preventing unauthorized users from creating accounts in your Prowler instance, making it more suitable for controlled enterprise environments.
