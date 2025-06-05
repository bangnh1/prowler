# Prowler UI Helm Chart

This Helm chart deploys the Prowler UI component, which provides a web interface for interacting with Prowler.

## Configuration

The Prowler UI Helm chart can be configured using the values in the `values.yaml` file. Here are some key configuration options:

### Authentication Options

The following authentication options are available:

- `secrets.DISABLE_SIGNUP`: Set to `true` to disable user registration functionality. When enabled, only administrators can create new user accounts. The default value is `false`, which allows users to self-register.

### Other Configuration Options

- `secrets.SITE_URL`: The URL where the Prowler UI will be accessible.
- `secrets.API_BASE_URL`: The URL of the Prowler API.
- `secrets.AUTH_SECRET`: Secret key for authentication (generate with `openssl rand -base64 32`).

## Installation

You can install the Prowler UI chart with the following command:

```bash
helm install prowler-ui ./prowler-ui
```

To customize the installation, create a values file and specify it during installation:

```bash
helm install prowler-ui ./prowler-ui -f my-values.yaml
```

## Disabling User Registration

To disable user registration (sign-up) functionality:

1. Set `secrets.DISABLE_SIGNUP` to `true` in your values file:

```yaml
secrets:
  DISABLE_SIGNUP: true
```

2. Install or upgrade the Helm chart with your values file:

```bash
helm upgrade --install prowler-ui ./prowler-ui -f my-values.yaml
```

With this configuration, new users won't be able to register themselves, and the sign-up page will redirect to the login page. The sign-up link will also be hidden from the login page.
