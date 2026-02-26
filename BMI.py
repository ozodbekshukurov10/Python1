
AI Gateway hujjatlarini o'qing
Misol: OpenAI yordamida alternativ matn yaratish
import OpenAI from "openai";

export default async (req: Request) => {
  if (req.method !== "POST") {
    return new Response("Method not allowed", { status: 405 });
  }

  try {
    const { description } = await req.json();
    if (!description) {
      return new Response("Missing description", { status: 400 });
    }

    const client = new OpenAI();
    const res = await client.responses.create({
      model: "gpt-5-mini",
      input: [
        { role: "user", content: `Write concise alt text for: ${description}` },
      ],
    });

    return Response.json({ altText: res.output_text });
  } catch {
    return new Response("Server error", { status: 500 });
  }
};

export const config = {
  path: "/api/alt-text",
};