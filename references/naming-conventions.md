# Naming Conventions Reference

Quick reference for self-documenting names. Good names eliminate the need for comments.

---

## Functions

### Pattern: `verbNoun` or `verbNounModifier`

| Purpose | Pattern | Examples |
|---------|---------|----------|
| Get data | `get[Thing]` | `getUser`, `getUserById`, `getActiveOrders` |
| Get computed | `calculate[Thing]` | `calculateTotal`, `calculateTaxRate` |
| Create | `create[Thing]` | `createUser`, `createOrderFromCart` |
| Update | `update[Thing]` | `updateUserEmail`, `updateOrderStatus` |
| Delete | `delete[Thing]` / `remove[Thing]` | `deleteUser`, `removeItemFromCart` |
| Check state | `is[Condition]` / `has[Thing]` / `can[Action]` | `isValid`, `hasPermission`, `canEdit` |
| Validate | `validate[Thing]` | `validateEmail`, `validateUserInput` |
| Convert | `[source]To[target]` | `jsonToXml`, `celsiusToFahrenheit` |
| Format | `format[Thing]` | `formatDate`, `formatCurrency` |
| Parse | `parse[Thing]` | `parseJson`, `parseQueryString` |
| Find | `find[Thing]` | `findUserByEmail`, `findMatchingRecords` |
| Filter | `filter[Things]By[Criteria]` | `filterUsersByRole`, `filterActiveItems` |
| Handle events | `handle[Event]` / `on[Event]` | `handleSubmit`, `onClick`, `onUserCreated` |
| Send | `send[Thing]` | `sendEmail`, `sendNotification` |
| Load | `load[Thing]` | `loadConfiguration`, `loadUserPreferences` |
| Save | `save[Thing]` | `saveDocument`, `saveUserSettings` |
| Init | `initialize[Thing]` | `initializeApp`, `initializeDatabase` |

---

## Variables

### General

| Type | Pattern | Examples |
|------|---------|----------|
| Single item | Singular noun | `user`, `order`, `product` |
| Collection | Plural noun | `users`, `orders`, `products` |
| Count | `[thing]Count` | `userCount`, `errorCount` |
| Index | `[thing]Index` | `currentIndex`, `selectedIndex` |
| Map/Dictionary | `[key]To[Value]` or `[thing]Map` | `userIdToName`, `productMap` |
| Configuration | `[thing]Config` / `[thing]Options` | `apiConfig`, `renderOptions` |

### Booleans — Always a Question

| Pattern | Examples |
|---------|----------|
| `is[State]` | `isLoading`, `isValid`, `isAuthenticated`, `isEmpty` |
| `has[Thing]` | `hasPermission`, `hasErrors`, `hasChildren` |
| `can[Action]` | `canEdit`, `canDelete`, `canSubmit` |
| `should[Action]` | `shouldUpdate`, `shouldRender`, `shouldRetry` |
| `was[State]` | `wasSuccessful`, `wasModified` |
| `will[Action]` | `willExpire`, `willRedirect` |

---

## Classes & Types

| Element | Pattern | Examples |
|---------|---------|----------|
| Class | `PascalCase`, noun | `UserService`, `PaymentProcessor`, `OrderRepository` |
| Interface | `PascalCase`, noun | `UserCredentials`, `ApiResponse`, `ConfigOptions` |
| Type | `PascalCase`, noun | `UserId`, `OrderStatus`, `ValidationResult` |
| Enum | `PascalCase` | `UserRole`, `PaymentStatus`, `HttpMethod` |
| Enum values | `PascalCase` or `SCREAMING_SNAKE` | `UserRole.Admin` or `USER_ROLE_ADMIN` |

---

## Constants

### Pattern: `SCREAMING_SNAKE_CASE`

```typescript
const MAX_LOGIN_ATTEMPTS = 3;
const DEFAULT_TIMEOUT_MS = 5000;
const API_BASE_URL = 'https://api.example.com';
const SECONDS_PER_DAY = 86400;
const SUPPORTED_FILE_TYPES = ['jpg', 'png', 'gif'];
```

---

## Files & Folders

| Type | Pattern | Examples |
|------|---------|----------|
| Module folder | `kebab-case` | `user-auth/`, `payment-processing/` |
| Code files | `kebab-case` | `user-service.ts`, `api-client.js` |
| Component files | `PascalCase` | `UserProfile.tsx`, `NavBar.vue` |
| Test files | `[name].test.[ext]` | `user-service.test.ts` |
| Type files | `types.[ext]` or `[name].types.[ext]` | `types.ts`, `user.types.ts` |
| Config files | `[tool].config.[ext]` | `eslint.config.js`, `tsconfig.json` |

---

## Avoid These

| Bad | Why | Good |
|-----|-----|------|
| `data` | Too vague | `userData`, `apiResponse`, `formValues` |
| `info` | Too vague | `userInfo` → `userProfile` |
| `temp` | Unclear purpose | `pendingOrder`, `unsavedChanges` |
| `x`, `y`, `a`, `b` | Meaningless | `width`, `height`, `source`, `target` |
| `doStuff()` | No information | `processPayment()`, `validateForm()` |
| `handleClick()` | Missing context | `handleLoginClick()`, `handleDeleteItem()` |
| `flag` | Boolean what? | `isEnabled`, `hasAccess` |
| `list` | List of what? | `userList` → `users` |
| `manager` | Overloaded term | Be specific: `UserAuthenticator`, `OrderProcessor` |
| `utils` | Junk drawer | Split into focused modules |

---

## Abbreviations to Avoid

| Avoid | Use |
|-------|-----|
| `btn` | `button` |
| `msg` | `message` |
| `err` | `error` |
| `req` / `res` | `request` / `response` (except in middleware signatures) |
| `cfg` / `conf` | `config` |
| `num` | `count` or specific: `orderNumber` |
| `idx` | `index` |
| `arr` | Name the contents: `items`, `users` |
| `obj` | Name the type: `user`, `config` |
| `str` | Name the content: `username`, `filePath` |

---

## Acceptable Short Names

| Name | When OK |
|------|---------|
| `i`, `j`, `k` | Loop indices in short loops |
| `e` / `err` | Catch block error parameter |
| `id` | Universal abbreviation |
| `db` | Database references |
| `api` | API references |
| `url` | URL strings |
| `io` | Input/output |
| `fs` | File system |

---

*Names should tell a story. — Programmatron 💻*
