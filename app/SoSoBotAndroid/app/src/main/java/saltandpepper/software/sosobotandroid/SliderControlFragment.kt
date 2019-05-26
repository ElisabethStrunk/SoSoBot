package saltandpepper.software.sosobotandroid

import android.content.Context
import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.SeekBar
import kotlinx.android.synthetic.main.fragment_slider_control.*

/**
 * A simple [Fragment] subclass.
 * Activities that contain this fragment must implement the
 * [SliderControlFragment.OnFragmentInteractionListener] interface
 * to handle interaction events.
 *
 */
class SliderControlFragment : Fragment(), SeekBar.OnSeekBarChangeListener {
    private var listener: OnFragmentInteractionListener? = null

    private val offset = 100
    private var previousProgress = offset

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_slider_control, container, false)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        leftRightSeekBar.setOnSeekBarChangeListener(this)
        upDownSeekBar.setOnSeekBarChangeListener(this)
    }

    override fun onAttach(context: Context) {
        super.onAttach(context)
        if (context is OnFragmentInteractionListener) {
            listener = context
        } else {
            throw RuntimeException(context.toString() + " must implement OnFragmentInteractionListener")
        }
    }

    override fun onDetach() {
        super.onDetach()
        listener = null
    }

    override fun onProgressChanged(seekBar: SeekBar?, progress: Int, fromUser: Boolean) {
        if (!fromUser || progress == previousProgress) {
            return
        }

        val power = if (progress > offset) progress - offset else offset - progress
        val direction: Direction = when (seekBar) {
            leftRightSeekBar -> when {
                progress > offset -> { // right
                    Direction.RIGHT
                }
                progress < offset -> { // left
                    Direction.LEFT
                }
                else -> { // stop
                    if (previousProgress > offset) Direction.RIGHT else Direction.LEFT
                }
            }
            upDownSeekBar -> when { // TODO isn't called
                progress > offset -> { // up
                    Direction.FORWARD
                }
                progress < offset -> { // down
                    Direction.BACKWARD
                }
                else -> { // stop
                    if (previousProgress > offset) Direction.FORWARD else Direction.BACKWARD
                }
            }
            else -> return
        }
        listener?.onFragmentInteraction(direction, power)
        previousProgress = progress
    }

    override fun onStartTrackingTouch(seekBar: SeekBar?) {
    }

    override fun onStopTrackingTouch(seekBar: SeekBar?) {
        seekBar?.setProgress(offset, true)
    }

    /**
     * This interface must be implemented by activities that contain this
     * fragment to allow an interaction in this fragment to be communicated
     * to the activity and potentially other fragments contained in that
     * activity.
     *
     *
     * See the Android Training lesson [Communicating with Other Fragments]
     * (http://developer.android.com/training/basics/fragments/communicating.html)
     * for more information.
     */
    interface OnFragmentInteractionListener {
        fun onFragmentInteraction(direction: Direction, power: Int)
    }
}
