import logging
from abc import abstractmethod

from blackfennec.actions import Action
from blackfennec.structure.structure import Structure
from gi.repository import Gtk, Adw, Gio, Gdk

from blackfennec.actions.context import Context
from blackfennec.interpretation.interpretation import Interpretation

logger = logging.getLogger(__name__)


class ActionItemView:
    """View for a key value pair of a map."""

    def __init__(
            self,
            interpretation: Interpretation,
            view_model,
    ):
        """Create map item view.

        Args:
            key: The key of the map item.
            interpretation (Interpretation): The preview.
            view_model (ListViewModel): view model.

        """

        self._interpretation = interpretation
        self._view_model = view_model
        self._selected = None
        self._popover = None

        self._add_right_click_controller()

    @property
    @abstractmethod
    def action_row(self) -> Adw.ActionRow:
        """The action row of the view"""
        pass

    @property
    @abstractmethod
    def popover_parent(self) -> Gtk.Box:
        """The parent of the popover"""
        pass

    @property
    def selected(self):
        return self._selected

    @selected.setter
    def selected(self, value):
        self._selected = value
        style = self.action_row.get_style_context()
        if self.selected:
            style.add_class('card')
        else:
            style.remove_class('card')

    def _add_right_click_controller(self):
        gesture = Gtk.GestureClick.new()
        gesture.set_button(3)
        gesture.connect('released', self._on_context_menu_pressed)
        self.action_row.add_controller(gesture)

    def _on_context_menu_pressed(self, gesture, n_press, x, y):
        if self._popover is None:
            structure = self._interpretation.structure

            actions = self._view_model.get_actions(structure)
            if not actions:
                logger.info("No actions available")
                return

            menu = self._create_context_menu(structure, actions)
            self._popover = Gtk.PopoverMenu.new_from_model(menu)

            self.popover_parent.append(self._popover)
            self._popover.present()
            allocation = self.action_row.get_allocation()
            self._popover.set_offset(0, allocation.height - 5)
            self._popover.set_pointing_to(Gdk.Rectangle(0, 0, 0, 0))

        self._popover.popup()

    def _create_context_menu(self, structure: Structure, actions: list[Action]):
        context = Context(structure)

        menu = Gio.Menu().new()
        action_map = Gio.SimpleActionGroup.new()
        action_group_name = f'core-map-{hash(structure.parent)}-child-{hash(structure)}'

        action_lookup = {}
        for action in actions:
            action_name = action.name.replace(' ', '_')
            full_action_name = f'{action_group_name}.{action_name}'
            menu_item = Gio.MenuItem.new(action.name, full_action_name)
            menu.append_item(menu_item)

            def execute_action(action: Gio.SimpleAction, unused_param, unused_data):
                logger.info(f"Executing {action.get_name()} on {context.structure}")
                action_lookup[action.get_name()].execute(context)

            action_lookup[action_name] = action
            action_map.add_action_entries([
                (action_name, execute_action)
            ])

        menu.freeze()

        self.action_row.insert_action_group(action_group_name, action_map)
        return menu
