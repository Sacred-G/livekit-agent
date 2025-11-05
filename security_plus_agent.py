"""
LiveKit Security+ Exam Teaching Assistant
==========================================
An interactive voice agent that helps students prepare for the CompTIA Security+ exam.
"""

from dotenv import load_dotenv
from livekit import agents
from livekit.agents import Agent, AgentSession, RunContext
from livekit.agents.llm import function_tool
from livekit.plugins import openai, deepgram, silero
import os
import random
from domains import ALL_DOMAINS
from security_plus_knowledge_base import PRACTICE_QUESTIONS

# Load environment variables
load_dotenv(".env")

class SecurityPlusTeacher(Agent):
    """Security+ exam teaching assistant with comprehensive knowledge base."""

    def __init__(self):
        super().__init__(
            instructions="""
You are a certified CompTIA Security+ instructor conducting an engaging, voice-based class.  
You are beginning a live CompTIA Security+ class. Introduce yourself as the instructor and start the first session naturally, just as a real teacher would at the beginning of a course. Speak with warmth, confidence, and clear pacing.

Your introduction should:
1. Greet the class naturally. Vary how you open each time (examples: "Good morning everyone", "Hey folks, welcome in", "Alright team, let's get started").
2. Introduce yourself as their Security+ instructor and mention that you'll be guiding them through the certification topics.
3. Briefly explain what today's session will cover — keep it conversational, not scripted.
4. Set expectations: mention note-taking, participation, and pacing.
5. Add small, human details that sound spontaneous ("Let me grab a sip of water", "If you have a notebook handy, go ahead and open it").
6. Use natural pauses and phrasing cues like [break:1s] and [break:2s] to allow for realism in delivery.
7. End your introduction by smoothly transitioning into the first topic — don't sound robotic or read off bullet points.

Example pattern (do not repeat exactly):
"Good morning, everyone! [break:1s] My name is Alex, and I'll be your instructor for the CompTIA Security+ course. I'm really excited to walk you through some core cybersecurity concepts — we'll break things down piece by piece, and I promise to keep it approachable. [break:1s] Today, we'll start with the fundamentals: understanding what security actually means, and the principles that guide it — confidentiality, integrity, and availability. [break:1s] Make sure you've got a way to take notes; I'll pause along the way so you can jot down the key points. [break:2s] Alright, let's dive in."

Tone Guidelines:
- Never sound like you're reading a script.
- Vary your openings, word choices, and transitions each time.
- Be conversational, approachable, and adaptive — sound human.
- Keep your energy calm but confident, and your explanations clear.
- Speak at a steady, natural pace; avoid rushing or monotone delivery.


Instructor Personality
- Speak conversationally and naturally, like a real teacher in front of a classroom.
- Be patient, encouraging, and confident.
- Vary your tone and rhythm to keep the audience's attention.
- Address the class occasionally ("everyone", "folks", "team") to create presence.
- Avoid robotic repetition — change how you open, explain, pause, and summarize each time.

Teaching Flow (Flexible)
Instead of following a rigid pattern, alternate between different structures.  
Use these as interchangeable approaches so lessons stay fresh:

A) Classic Flow:
1. Introduce the topic and explain why it matters.
2. Cover 2–3 major points with clear explanations.
3. Insert a short pause for note-taking: [break:1.5s]
4. Ask for understanding or reflection: [checkpoint]
5. Provide a scenario or story.
6. Recap with practical takeaways: [recap]

B) Example-First Flow:
1. Start with a short real-world scenario or story.
2. Ask the students to think about what they would do.
3. Explain the core concept that applies to that example.
4. Pause briefly: [break:1.5s]
5. Add an exam connection or memory cue: [exam]
6. Summarize with the main lesson point.

C) Interactive Flow:
1. Ask a question to spark curiosity.
2. Explain the concept piece by piece, answering your own question.
3. Insert mini-pauses between points: [break:1s]
4. Offer a "think about this" moment: [checkpoint]
5. End with a short recap or exam-style tip.

Adaptive Teaching
- Rephrase difficult ideas in simpler language if the topic is dense.
- Use analogies, comparisons, and relatable examples.
- Reinforce learning by saying: "Let's look at that another way," or "Here's a different example."
- Acknowledge confusion gently and re-explain with patience.
- Use natural transitions like "Before we wrap up..." or "Let's take another angle."

Scenario and Storytelling
- Use realistic cybersecurity situations ("Imagine a small business hit by ransomware...").
- Reference job roles and decision-making contexts (analyst, sysadmin, SOC lead).
- When introducing examples, vary openings ("Let's consider a case where..." / "Picture this scenario...").

Exam Connection
- Mention relevant Security+ domains (e.g., Domain 1.2, control types).
- Use [exam] before exam-related hints for later highlighting.
- Offer different memory strategies each time: mnemonics, contrasts, or associations.

Voice and Timing Cues
- Speak at a natural pace with deliberate pauses.
- Use [break:1s] or [break:2s] for silence and reflection.
- Use [emph] and [/emph] to mark emphasis.
- Use [slow] and [/slow] when defining or quoting critical terms.
- Randomize transitions — don't always start with "Okay" or "Next."  
  Try alternatives like "Let's dive in," "Here's what matters most," or "Let's step through it slowly."

Classroom Energy
- Encourage students regularly ("Good question,", "Excellent observation,", "That's an important point.")
- Comment on progress with variation ("We're halfway through this concept,", "That was a big one, nice job.")
- Occasionally recap earlier material for continuity.

Guardrails
- Avoid predictable speech patterns.
- Mix short, punchy explanations with longer, reflective ones.
- After every concept, allow time for note-taking or questions.
- Keep lessons concise and human — your goal is mastery, not memorization.

Your mission: Deliver each session with authenticity and variety.  
Vary structure, tone, and pacing naturally so the class feels spontaneous and real.
"""
)



        # Initialize knowledge base and tracking from imported data
        self.knowledge_base = ALL_DOMAINS
        self.practice_questions = PRACTICE_QUESTIONS
        self.student_progress = {
            "questions_answered": 0,
            "correct_answers": 0,
            "topics_covered": set()
        }

    @function_tool
    async def get_exam_overview(self, context: RunContext) -> str:
        """Get overview of Security+ exam structure."""
        overview = "CompTIA Security+ (SY0-701) Exam:\n\n"
        overview += "• 90 questions (multiple choice and performance-based)\n"
        overview += "• 90 minutes duration\n"
        overview += "• Passing Score: 750 (scale 100-900)\n\n"
        overview += "Domains:\n"
        
        for domain_id, domain in self.knowledge_base.items():
            overview += f"• {domain['name']} - {domain['weight']}\n"
        
        return overview

    @function_tool
    async def explain_topic(self, context: RunContext, domain: str, topic: str) -> str:
        """Explain a specific Security+ topic.
        
        Args:
            domain: Domain number (domain_1 through domain_5)
            topic: Topic name (e.g., malware, cryptography)
        """
        domain = domain.lower().replace(" ", "_")
        topic = topic.lower().replace(" ", "_")
        
        if domain not in self.knowledge_base:
            return "Use domain_1 through domain_5"
        
        domain_data = self.knowledge_base[domain]
        
        if topic not in domain_data["topics"]:
            available = ", ".join(domain_data["topics"].keys())
            return f"Available topics: {available}"
        
        topic_data = domain_data["topics"][topic]
        self.student_progress["topics_covered"].add(f"{domain}_{topic}")
        
        explanation = f"📚 {topic.replace('_', ' ').title()}\n\n"
        explanation += f"{topic_data.get('description', '')}\n\n"
        
        # Iterate through all fields except description and key_points
        for field_name, field_data in topic_data.items():
            if field_name in ["description", "key_points"]:
                continue
            
            if isinstance(field_data, list):
                # Format field name for display
                display_name = field_name.replace("_", " ").title()
                explanation += f"{display_name}:\n"
                for item in field_data[:6]:  # Show up to 6 items
                    explanation += f"• {item}\n"
                explanation += "\n"
        
        if "key_points" in topic_data:
            explanation += "🎯 Key Points:\n"
            for point in topic_data["key_points"]:
                explanation += f"• {point}\n"
        
        return explanation

    @function_tool
    async def list_topics(self, context: RunContext, domain: str) -> str:
        """List all topics in a domain.
        
        Args:
            domain: Domain number (domain_1 through domain_5)
        """
        domain = domain.lower().replace(" ", "_")
        
        if domain not in self.knowledge_base:
            return "Use: domain_1, domain_2, domain_3, domain_4, or domain_5"
        
        domain_data = self.knowledge_base[domain]
        result = f"{domain_data['name']} ({domain_data['weight']})\n\n"
        
        for topic_key, topic_data in domain_data["topics"].items():
            result += f"• {topic_key}: {topic_data['description']}\n"
        
        return result

    @function_tool
    async def teach_lesson(self, context: RunContext, domain: str, topic: str) -> str:
        """Start a structured lesson on a specific topic with teaching format.
        
        Args:
            domain: Domain number (domain_1 through domain_5)
            topic: Topic name (e.g., malware, cryptography)
        """
        domain = domain.lower().replace(" ", "_")
        topic = topic.lower().replace(" ", "_")
        
        if domain not in self.knowledge_base:
            return "Use domain_1 through domain_5"
        
        domain_data = self.knowledge_base[domain]
        
        if topic not in domain_data["topics"]:
            available = ", ".join(domain_data["topics"].keys())
            return f"Available topics: {available}"
        
        topic_data = domain_data["topics"][topic]
        self.student_progress["topics_covered"].add(f"{domain}_{topic}")
        
        lesson = f"📚 Today's Lesson: {topic.replace('_', ' ').title()}\n\n"
        lesson += f"Alright class, today we're going to cover {topic.replace('_', ' ')}. This is an important topic for your Security+ exam.\n\n"
        lesson += f"Let me start with the fundamentals. {topic_data.get('description', '')}\n\n"
        lesson += "Let me pause here for a moment so you can write that down.\n\n"
        
        # Iterate through all list fields except key_points
        field_count = 0
        for field_name, field_data in topic_data.items():
            if field_name in ["description", "key_points"] or not isinstance(field_data, list):
                continue
            
            field_count += 1
            display_name = field_name.replace("_", " ")
            
            if field_count == 1:
                lesson += f"Now, let me walk you through the {display_name} you need to know:\n\n"
            else:
                lesson += f"Next, let's look at the {display_name}:\n\n"
            
            for i, item in enumerate(field_data[:5], 1):  # Show up to 5 items
                lesson += f"{i}. {item}\n"
            lesson += "\nTake a moment to note these down. These are exam favorites.\n\n"
        
        if "key_points" in topic_data:
            lesson += "🎯 Here are the critical points you absolutely must remember:\n\n"
            for point in topic_data["key_points"]:
                lesson += f"• {point}\n"
            lesson += "\nThese often appear on the exam, so highlight them in your notes.\n\n"
        
        lesson += "Now, before we move on - do you have any questions about what we've covered so far?"
        
        return lesson

    @function_tool
    async def deliver_scripted_lesson(self, context: RunContext, domain: str, topic: str) -> str:
        """Deliver a pre-written scripted lesson for a topic (if available).
        
        Args:
            domain: Domain number (domain_1 through domain_5)
            topic: Topic name (e.g., security_controls, cryptography)
        """
        domain = domain.lower().replace(" ", "_")
        topic = topic.lower().replace(" ", "_")
        
        if domain not in self.knowledge_base:
            return "Use domain_1 through domain_5"
        
        domain_data = self.knowledge_base[domain]
        
        if topic not in domain_data["topics"]:
            available = ", ".join(domain_data["topics"].keys())
            return f"Available topics: {available}"
        
        topic_data = domain_data["topics"][topic]
        
        # Check if topic has a scripted lesson
        if "scripted_lesson" not in topic_data:
            return f"No scripted lesson available for {topic}. Try using 'teach_lesson' or 'explain_topic' instead."
        
        self.student_progress["topics_covered"].add(f"{domain}_{topic}")
        
        # Deliver the scripted lesson
        lesson = f"📚 Scripted Lesson: {topic.replace('_', ' ').title()}\n\n"
        lesson += f"Domain: {domain_data['name']}\n\n"
        lesson += topic_data["scripted_lesson"]
        
        return lesson

    @function_tool
    async def quiz_me(self, context: RunContext, num_questions: int = 1) -> str:
        """Start practice quiz.
        
        Args:
            num_questions: Number of questions (1-5)
        """
        num_questions = min(max(1, num_questions), 5)
        questions = random.sample(self.practice_questions, min(num_questions, len(self.practice_questions)))
        
        quiz_text = f"📝 Practice Quiz - {num_questions} Question(s)\n\n"
        
        for i, q in enumerate(questions, 1):
            quiz_text += f"Q{i}: {q['question']}\n"
            for option in q['options']:
                quiz_text += f"{option}\n"
            quiz_text += "\n"
        
        quiz_text += "Tell me your answer(s) - e.g., 'A' or 'B, C, A'"
        context.store_metadata("current_quiz", questions)
        
        return quiz_text

    @function_tool
    async def check_answer(self, context: RunContext, answer: str) -> str:
        """Check quiz answers.
        
        Args:
            answer: Your answer(s) (e.g., 'A' or 'B, C, A')
        """
        current_quiz = context.get_metadata("current_quiz")
        
        if not current_quiz:
            return "No active quiz. Use quiz_me first!"
        
        answers = [a.strip().upper() for a in answer.split(",")]
        
        if len(answers) != len(current_quiz):
            return f"Provide {len(current_quiz)} answer(s)"
        
        results = "📊 Results:\n\n"
        correct_count = 0
        
        for i, (ans, q) in enumerate(zip(answers, current_quiz), 1):
            is_correct = ans == q['correct']
            if is_correct:
                correct_count += 1
                self.student_progress["correct_answers"] += 1
                results += f"Q{i}: ✓ Correct!\n"
            else:
                results += f"Q{i}: ✗ Wrong. Answer: {q['correct']}\n"
            
            results += f"{q['explanation']}\n\n"
            self.student_progress["questions_answered"] += 1
        
        score = (correct_count / len(current_quiz)) * 100
        results += f"Score: {correct_count}/{len(current_quiz)} ({score:.0f}%)\n"
        
        if score == 100:
            results += "🎉 Perfect!"
        elif score >= 70:
            results += "👍 Good work!"
        else:
            results += "📚 Keep studying!"
        
        context.store_metadata("current_quiz", None)
        return results

    @function_tool
    async def get_study_tips(self, context: RunContext) -> str:
        """Get study tips for Security+ exam."""
        tips = "🎓 Security+ Study Tips:\n\n"
        tips += "1. Understand concepts, don't just memorize\n"
        tips += "2. Use acronyms (CIA, AAA, etc.)\n"
        tips += "3. Practice hands-on labs\n"
        tips += "4. Focus on high-weight domains (25% and 24%)\n"
        tips += "5. Read questions carefully on exam day\n"
        tips += "6. Watch for key words: BEST, MOST, FIRST\n"
        tips += "7. Performance-based questions come first\n"
        tips += "8. Flag difficult questions and return later\n"
        return tips

    @function_tool
    async def get_progress(self, context: RunContext) -> str:
        """Check your study progress."""
        progress = "📈 Your Progress:\n\n"
        progress += f"Questions Answered: {self.student_progress['questions_answered']}\n"
        progress += f"Correct: {self.student_progress['correct_answers']}\n"
        
        if self.student_progress['questions_answered'] > 0:
            accuracy = (self.student_progress['correct_answers'] / self.student_progress['questions_answered']) * 100
            progress += f"Accuracy: {accuracy:.1f}%\n"
        else:
            progress += "Accuracy: N/A\n"
        
        progress += f"\nTopics Covered: {len(self.student_progress['topics_covered'])}\n"
        
        return progress


async def entrypoint(ctx: agents.JobContext):
    """Entry point for the agent."""

    # Configure the voice pipeline with the essentials
    session = AgentSession(
        stt=deepgram.STT(model="nova-2"),
        llm=openai.LLM(model=os.getenv("LLM_CHOICE", "gpt-4.1-mini")),
        tts=openai.TTS(voice="echo"),
        vad=silero.VAD.load(),
    )

    # Start the session
    await session.start(
        room=ctx.room,
        agent=SecurityPlusTeacher()
    )

    # Generate initial greeting
    await session.generate_reply(
        instructions="""Greet the class warmly as a teacher would at the start of a lesson.
        Introduce yourself as their Security+ instructor and welcome them to today's class.
        Ask them what topic they'd like to cover today, or if they'd like you to start with a particular domain.
        Be encouraging and create a classroom atmosphere."""
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
