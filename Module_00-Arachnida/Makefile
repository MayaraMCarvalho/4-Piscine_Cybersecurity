# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: macarval <macarval@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/19 16:33:22 by macarval          #+#    #+#              #
#    Updated: 2025/11/12 12:05:29 by macarval         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Regular colors
RED			= \033[0;31m
GREEN		= \033[0;32m
YELLOW		= \033[0;33m
BLUE		= \033[0;34m
PURPLE		= \033[0;35m
CYAN		= \033[0;36m
WHITE		= \033[0;37m
RESET		= \033[0m

# Bold
BRED		= \033[1;31m
BGREEN		= \033[1;32m
BYELLOW		= \033[1;33m
BBLUE		= \033[1;34m
BPURPLE		= \033[1;35m
BCYAN		= \033[1;36m
BWHITE		= \033[1;37m

NAME		= arachnida
SPIDER		= spider
SCORPION	= scorpion

DATA_PATH	= ./data/

# --- Python Configuration ---
VENV_DIR	= .venv
PYTHON		= $(VENV_DIR)/bin/python3
PIP			= $(VENV_DIR)/bin/pip

# --- Rules ---
all: 		$(VENV_DIR)

$(VENV_DIR):	requirements.txt
	@echo "Creating virtual environment in $(VENV_DIR)..."
	@sudo python3 -m venv $(VENV_DIR) > /dev/null 2>&1
	@echo "Installing dependencies from requirements.txt..."
	@$(PIP) install --upgrade pip > /dev/null 2>&1
	@$(PIP) install -r requirements.txt > /dev/null 2>&1
	@echo "$(CYAN)$(NAME): $(GREEN)Virtual environment and dependencies installed!$(RESET)"

$(DATA_PATH):
			@mkdir -p $(DATA_PATH)

# --- Execution Rules ---
run_spider:	$(VENV_DIR)
	@$(PYTHON) $(SPIDER) $(ARGS)

run_scorpion:	$(VENV_DIR)
	@$(PYTHON) $(SCORPION) $(ARGS)

# --- Clean Rules ---
clean:
	@rm -rf $(DATA_PATH)
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@echo "$(CYAN)$(NAME): $(GREEN)Clean done!$(RESET)"

fclean:		clean
	@rm -rf $(VENV_DIR)
	@echo "$(CYAN)$(NAME): $(GREEN)Full clean done!$(RESET)"


re:			fclean all

git:
	clear
	@make --no-print-directory fclean
	@git add .
	@git status
	@echo "$(BPURPLE)Choose the commit type:"; \
	echo "$(BYELLOW)1. feat: $(WHITE)Adds a new feature to your codebase"; \
	echo "$(BYELLOW)2. fix: $(WHITE)Solves a problem in your codebase"; \
	echo "$(BYELLOW)3. docs: $(WHITE)Documentation changes"; \
	echo "$(BYELLOW)4. style: $(WHITE)Formatting, spacing, etc."; \
	echo "$(BYELLOW)5. refactor: $(WHITE)Refactoring code used in production, e.g. renaming a variable"; \
	echo "$(BYELLOW)6. test: $(WHITE)Adding tests, refactoring tests"; \
	echo "$(BYELLOW)7. chore: $(WHITE)Adjust build script, updating dependencies, makefile etc"; \
	read type_choice; \
	case $$type_choice in \
				1) type="feat" ;; \
				2) type="fix" ;; \
				3) type="docs" ;; \
				4) type="style" ;; \
				5) type="refactor" ;; \
				6) type="test" ;; \
				7) type="chore" ;; \
				*) echo "$(BRED)Invalid choice"; exit 1 ;; \
	esac; \
	echo -n "\n"; \
	echo "$(MAGENTA)Enter the exercise:"; \
	read ex; \
	echo -n "\n"; \
	echo "$(GREEN)Enter the commit message:"; \
	read msg; \
	echo -n "\n"; \
	echo "$(BLUE)"; \
	git commit -m "[$(NAME) - ex$$ex] $$type: $$msg"; \
	git push

.PHONY:		all re clean fclean git run_spider run_scorpion
