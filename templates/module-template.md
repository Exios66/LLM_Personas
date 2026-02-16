# Module Template

Use this template when creating new code modules. Copy and adapt as needed.

---

## Module Header

```
/**
 * Module: [ModuleName]
 * Purpose: [Single sentence describing what this module does]
 * 
 * Dependencies: [List external dependencies]
 * Exports: [List public functions/classes]
 * 
 * Usage:
 *   import { functionName } from './moduleName';
 *   const result = functionName(params);
 */
```

## Module Structure

```
[module-name]/
├── index.[ext]           # Public API exports
├── [module-name].[ext]   # Core implementation
├── types.[ext]           # Type definitions (if applicable)
├── utils.[ext]           # Internal helper functions
└── [module-name].test.[ext]  # Tests
```

## Naming Conventions

| Element | Pattern | Example |
|---------|---------|---------|
| Module folder | kebab-case | `user-auth/` |
| Main file | kebab-case | `user-auth.ts` |
| Functions | camelCase, verb-first | `validateUserCredentials()` |
| Classes | PascalCase | `UserAuthService` |
| Constants | SCREAMING_SNAKE | `MAX_LOGIN_ATTEMPTS` |
| Types/Interfaces | PascalCase | `UserCredentials` |

## Template: Function Module

```typescript
// user-service.ts

// ============================================================
// TYPES
// ============================================================

interface User {
  id: string;
  email: string;
  createdAt: Date;
}

interface CreateUserParams {
  email: string;
  password: string;
}

// ============================================================
// CONSTANTS
// ============================================================

const DEFAULT_USER_ROLE = 'member';
const PASSWORD_MIN_LENGTH = 8;

// ============================================================
// CORE FUNCTIONS
// ============================================================

export function createUser(params: CreateUserParams): User {
  // Implementation
}

export function getUserById(userId: string): User | null {
  // Implementation
}

export function deleteUser(userId: string): boolean {
  // Implementation
}

// ============================================================
// INTERNAL HELPERS
// ============================================================

function hashPassword(plainText: string): string {
  // Implementation
}

function validateEmail(email: string): boolean {
  // Implementation
}
```

## Template: Class Module

```typescript
// payment-processor.ts

interface PaymentResult {
  success: boolean;
  transactionId: string | null;
  errorMessage: string | null;
}

export class PaymentProcessor {
  private apiKey: string;
  private baseUrl: string;

  constructor(apiKey: string, environment: 'sandbox' | 'production') {
    this.apiKey = apiKey;
    this.baseUrl = environment === 'production' 
      ? 'https://api.payment.com' 
      : 'https://sandbox.payment.com';
  }

  async processPayment(amount: number, currency: string): Promise<PaymentResult> {
    // Implementation
  }

  async refundPayment(transactionId: string): Promise<PaymentResult> {
    // Implementation
  }

  private buildAuthHeaders(): Record<string, string> {
    // Implementation
  }
}
```

## Checklist Before Committing Module

- [ ] Single responsibility - module does one thing well
- [ ] All public functions documented with purpose
- [ ] No placeholder or stub code
- [ ] Error cases handled explicitly
- [ ] No hardcoded secrets or environment-specific values
- [ ] Naming follows conventions above
- [ ] Index file exports only public API
