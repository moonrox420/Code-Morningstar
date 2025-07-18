FROM node:20-alpine

WORKDIR /app

COPY package.json tsconfig.json svelte.config.js ./
COPY src ./src
COPY public ./public

RUN npm install
RUN npm run build

CMD ["npm", "run", "preview", "--", "--host", "0.0.0.0", "--port", "5173"]