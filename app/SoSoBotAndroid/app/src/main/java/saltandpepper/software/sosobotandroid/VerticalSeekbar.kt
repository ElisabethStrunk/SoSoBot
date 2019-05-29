package saltandpepper.software.sosobotandroid

import android.content.Context
import android.graphics.Canvas
import android.util.AttributeSet
import android.view.MotionEvent
import android.widget.SeekBar

/**
 * Solution based on https://stackoverflow.com/questions/3333658/how-to-make-a-vertical-seekbar-in-android
 */
class VerticalSeekBar(context: Context, attrs: AttributeSet) : SeekBar(context, attrs) {

    private var mOnSeekBarChangeListener: OnSeekBarChangeListener? = null

    override fun onSizeChanged(w: Int, h: Int, oldw: Int, oldh: Int) {
        super.onSizeChanged(h, w, oldh, oldw)
    }

    override fun onMeasure(widthMeasureSpec: Int, heightMeasureSpec: Int) {
        super.onMeasure(heightMeasureSpec, widthMeasureSpec)
        setMeasuredDimension(measuredHeight, measuredWidth)
    }

    override fun onDraw(c: Canvas) {
        c.rotate(-90f)
        c.translate(-height.toFloat(),0f)

        super.onDraw(c)
    }

    override fun onTouchEvent(event: MotionEvent) : Boolean {
        if (!isEnabled) {
            return false
        }

        progress = max - (max * event.y / height).toInt()
        setProgress(progress, true)
        when (event.action) {
            MotionEvent.ACTION_DOWN -> mOnSeekBarChangeListener?.onStartTrackingTouch(this)
            MotionEvent.ACTION_MOVE -> mOnSeekBarChangeListener?.onProgressChanged(this, progress, true)
            MotionEvent.ACTION_UP -> mOnSeekBarChangeListener?.onStopTrackingTouch(this)
        }
        onSizeChanged(width, height, 0, 0)
        return true
    }

    override fun setOnSeekBarChangeListener(listener: OnSeekBarChangeListener) {
        mOnSeekBarChangeListener = listener
    }
}