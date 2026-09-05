# Code-Agent Security Review Checklist

Use this checklist when reviewing code produced or modified by an AI coding assistant.

## Secrets & credentials
- [ ] No hard-coded API keys, passwords, tokens or private keys
- [ ] Secrets are loaded from environment variables or a secret manager
- [ ] Example configuration uses placeholders only

## Input handling
- [ ] External input is validated and normalized
- [ ] SQL queries are parameterized
- [ ] HTML output is escaped where needed
- [ ] File paths are constrained and validated

## Process execution
- [ ] No unnecessary `shell=True`
- [ ] User-controlled values are not concatenated into commands
- [ ] Subprocess arguments are passed as structured lists where possible

## Networking
- [ ] TLS verification is enabled
- [ ] No insecure default bind address unless required
- [ ] Timeouts are configured
- [ ] Sensitive data is not logged

## Serialization & parsing
- [ ] No unsafe `eval` / `exec`
- [ ] No unsafe deserialization of untrusted data
- [ ] Parsers use safe modes and bounded input

## Authentication & authorization
- [ ] Authentication is not bypassed for convenience
- [ ] Authorization checks are enforced server-side
- [ ] Privileged actions are explicitly protected

## Dependencies
- [ ] Dependencies are pinned or constrained
- [ ] No unexplained/unmaintained dependency introduced
- [ ] Dependency scanning can be run in CI

## Error handling
- [ ] Errors do not expose credentials, stack traces or sensitive internals
- [ ] Security-relevant failures are logged appropriately

## Testing
- [ ] Security-sensitive code has unit/integration tests
- [ ] Negative and abuse cases are included
- [ ] Static-analysis checks can run automatically
